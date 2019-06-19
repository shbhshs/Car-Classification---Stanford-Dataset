# helper functions
def accuracy(y, pred_y, dim=1):
    #_, y_index = torch.max(y, dim=dim)
    _, y_index = y
    _, pred_y_index = torch.max(pred_y, dim=dim)
    num_correct = torch.sum(pred_y_index==y_index)
    acc = num_correct.item()/len(y)
    return acc

def precision(y, pred_y, dim=1):
    _, y_index = torch.max(y, dim=dim)
    _, pred_y_index = torch.max(pred_y, dim=dim)
    precision = precision_score(y_index.numpy(), pred_y_index.numpy(), average='micro')
    return precision

def recall(y, pred_y, dim=1):
    _, y_index = torch.max(y, dim=dim)
    _, pred_y_index = torch.max(pred_y, dim=dim)
    recall = recall_score(y_index.numpy(), pred_y_index.numpy(),average='micro')
    return recall

def test_accuracy(model, test_generator, use_gpu):
    acc = 0
    model.eval()
    for images,labels in test_generator:
        if use_gpu:
            images = images.cuda()
            labels = labels.cuda()
            labels = labels.type(torch.cuda.FloatTensor)
            
        output = model(images)
        acc += accuracy(output, labels)
        
    return(acc/len(test_generator))
