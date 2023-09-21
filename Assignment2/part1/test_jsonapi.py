import unittest
import jsonapi


def test_encode_complex():
    complex_num = complex(3, 4)
    actual = jsonapi.dumps(complex_num, cls=jsonapi.MyEncoder)
    assert actual == '{"real": 3.0, "imag": 4.0, "__extended_json_type__": "complex"}'


def test_decode_complex():
    encoded_complex_num = jsonapi.dumps(complex(4, 3), cls=jsonapi.MyEncoder)
    actual = jsonapi.loads(encoded_complex_num, cls=jsonapi.MyDecoder)
    assert actual == complex(4, 3)


def test_encode_range():
    test_range = range(100, 200, 2)
    actual = jsonapi.dumps(test_range, cls=jsonapi.MyEncoder)
    assert actual == '{"start": 100, "stop": 200, "step": 2, "__extended_json_type__": "range"}'


def test_decode_range():
    encoded_range = jsonapi.dumps(range(333, 444, 1), cls=jsonapi.MyEncoder)
    actual = jsonapi.loads(encoded_range, cls=jsonapi.MyDecoder)
    assert actual == range(333, 444, 1)