from imageai.Prediction.Custom import CustomImagePrediction
import io
import os
def image_pred(image):
    execution_path = os.getcwd()

    prediction = CustomImagePrediction()
    prediction.setModelTypeAsInceptionV3()
    prediction.setModelPath(os.path.join(execution_path, "model_ex-004_acc-0.492188.h5"))
    prediction.setJsonPath(os.path.join(execution_path, "model_class.json"))
    prediction.loadModel(num_objects=2)

    f = io.BytesIO(image)
    predictions, probabilities = prediction.predictImage(f, result_count=2)

    out = ("", 0)
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(eachPrediction , " : " , eachProbability)
    if probabilities[0] > probabilities[1]:
        return predictions[0]
    return eachPrediction[1]
