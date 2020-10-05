# -*- coding: utf-8 -*-
from django.shortcuts import render
from yolo.darkflow.darkflow.cli import cliHandler
from django.http import HttpResponse

# Create your views here.

# import tensorflow as tf
# from google.protobuf import text_format
# from tensorflow.python.platform import gfile

# import cv2
# import numpy as np
# from .darkflow.darkflow.net.build import TFNet

# import sys
# from .darkflow.darkflow.cli import cliHandler

# def index(request):

    # # Load Yolo
    
    # net = cv2.dnn.readNet("./my-tiny.weights", "./my-tiny.cfg")
    # classes = []
    # with open("labels.txt", "r") as f:
    #     classes = [line.strip() for line in f.readlines()]
    # layer_names = net.getLayerNames()
    # output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    # colors = np.random.uniform(0, 255, size=(len(classes), 3))

    # # Loading image
    # img = cv2.imread("sample.jpg")
    # img = cv2.resize(img, None, fx=0.4, fy=0.4)
    # height, width, channels = img.shape

    # # Detecting objects
    # blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    # net.setInput(blob)
    # outs = net.forward(output_layers)

    # # Showing informations on the screen
    # class_ids = []
    # confidences = []
    # boxes = []
    # for out in outs:
    #     for detection in out:
    #         scores = detection[5:]
    #         class_id = np.argmax(scores)
    #         confidence = scores[class_id]
    #         if confidence > 0.05:
    #             # Object detected
    #             center_x = int(detection[0] * width)
    #             center_y = int(detection[1] * height)
    #             w = int(detection[2] * width)
    #             h = int(detection[3] * height)

    #             # Rectangle coordinates
    #             x = int(center_x - w / 2)
    #             y = int(center_y - h / 2)

    #             boxes.append([x, y, w, h])
    #             confidences.append(float(confidence))
    #             class_ids.append(class_id)

    # indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.05, 0.04)

    # font = cv2.FONT_HERSHEY_PLAIN
    # for i in range(len(boxes)):
    #     if i in indexes:
    #         x, y, w, h = boxes[i]
    #         label = str(classes[class_ids[i]])
    #         color = colors[i]
    #         cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
    #         cv2.putText(img, label, (x, y + 30), font, 3, color, 3)


    # cv2.imshow("Image", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()




    # options = {"pbLoad": "built_graph/my-tiny.pb", "metaLoad": "built_graph/my-tiny.meta", "gpu": 0,"threshold": 0.2}

    # tfnet = TFNet(options)

    # imgcv = cv2.imread("sample.jpg")
    # result = tfnet.return_predict(imgcv)
    # context = {
    #     'result': result,
    # }


    # # cliHandler(sys.argv)

    # return render(request, 'yolo/index.html', context)

def index(request):
    image_name = 'sample.jpg'
    return HttpResponse(cliHandler(image_name))