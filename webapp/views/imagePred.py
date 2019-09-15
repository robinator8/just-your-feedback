from imageai.Prediction.Custom import CustomImagePrediction
import os
def image_pred(image):
    execution_path = os.getcwd()

    prediction = CustomImagePrediction()
    prediction.setModelTypeAsInceptionV3()
    prediction.setModelPath(os.path.join(execution_path, "model_ex-004_acc-0.492188.h5"))
    prediction.setJsonPath(os.path.join(execution_path, "model_class.json"))
    prediction.loadModel(num_objects=2)

    predictions, probabilities = prediction.predictImage(os.path.join(execution_path, "up.jpg"), result_count=2)
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(eachPrediction , " : " , eachProbability)
    if eachProbability[0] > execution_path[1]:
        return eachPrediction[0]
    return eachPrediction[1]
