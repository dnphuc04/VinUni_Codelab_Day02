"""Local tests do not claim to exercise Gemini."""
import importlib.util
import json
from pathlib import Path
from unittest.mock import patch
import pytest

spec = importlib.util.spec_from_file_location('prototype', Path(__file__).resolve().parents[1] / 'starter-code/prompt_prototype.py')
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)

@pytest.mark.parametrize('battery,expected', [(0,'dispatch_mobile_charger'),(4.9,'dispatch_mobile_charger'),(5,'draft_station_guidance'),(5.1,'draft_station_guidance'),(100,'draft_station_guidance'),(None,'request_information'),(-1,'request_information'),(101,'request_information'),(True,'request_information'),('2','request_information')])
def test_thresholds(battery, expected):
    context = p.case('test','hello',battery=battery,station=p.STATION)['context']
    assert p.required_action(context)[0] == expected

@pytest.mark.parametrize('change', [lambda d:d.update(action='draft_station_guidance'), lambda d:d.update(requires_human_approval=False), lambda d:d.update(missing_fields='bad'),lambda d:d.update(extra='bad'),lambda d:d.update(reason='')])
def test_reject_invalid_payload(change):
    context = p.TEST_CASES[0]['context']
    data = json.loads(p.fallback(context)[len(p.PREFIX):])
    change(data)
    with pytest.raises(ValueError):
        p.validate_output(p.PREFIX+json.dumps(data),context)

@pytest.mark.parametrize('raw', ['{}','text [DRAFT_ONLY]{}','[DRAFT_ONLY]not JSON'])
def test_bad_envelope(raw):
    with pytest.raises(ValueError):
        p.validate_output(raw,p.TEST_CASES[0]['context'])

def test_api_failure_is_not_success():
    with patch.object(p,'evaluate_prompt',side_effect=TimeoutError):
        result = p.run_case(p.TEST_CASES[0])
    assert result['passed'] is False
    assert result['fallback_used'] is True
    p.validate_output(result['delivered_output'],p.TEST_CASES[0]['context'])

def test_invalid_model_output_is_preserved_and_blocked():
    raw = '[DRAFT_ONLY]'+json.dumps({'action':'unsafe'})
    with patch.object(p,'evaluate_prompt',return_value=raw):
        result = p.run_case(p.TEST_CASES[0])
    assert result['raw_output'] == raw
    assert not result['passed']
    assert result['delivered_output'] != raw

def test_no_verified_station():
    context = p.case('test','hello',battery=30,station={**p.STATION,'verified':False})['context']
    assert p.required_action(context)[0] == 'manual_review'

def test_missing_location_requires_question():
    context = p.case('test','hello',location=None)['context']
    assert p.required_action(context) == ('request_information',['location'])
