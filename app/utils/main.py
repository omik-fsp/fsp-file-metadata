import os


def helloWorld():
    return 'Hello World!'


def handleFile(f):

    response = {}

    response['name'] = f.filename
    response['type'] = f.content_type
    # https://stackoverflow.com/questions/283707/size-of-an-open-file-object/283719#283719
    response['size'] = os.fstat(f.fileno()).st_size

    return response


def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
