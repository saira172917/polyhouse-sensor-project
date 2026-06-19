from src.predict import predict_yield

def test_prediction():
    result = predict_yield(22, 80, 900)
    assert result > 0