import os
import errno
#import psutil
import numpy as np


def mkdir_p(path):
    """ Equivalent of mkdir -p """
    """ source: http://bit.ly/1dyli3d """
    try:
        os.makedirs(path)
    except OSError as exc:   # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


# def memory_usage():
#     """ return the memory usage in MB """
#     """ source: http://bit.ly/1dspz7I """
#     process = psutil.Process(os.getpid())
#     try:
#         mem = process.get_memory_info()[0] / float(2 ** 20)
#     except:
#         mem = process.memory_info()[0] / float(2 ** 20)
#     return mem


def wc_l(fname):
    """ return number of lines in a file """

    lineCount = 0
    try:
        with open(fname, 'r') as f:
            for line in f:
                lineCount = lineCount + 1
    except:
        print('Could not open file ', fname)
        pass
    return lineCount


def git_version():
    """ returns git revision """
    """ source: http://bit.ly/1Ctm1ho """

    from subprocess import Popen, PIPE
    gitproc = Popen(['git', 'rev-parse', 'HEAD'], stdout=PIPE)
    (stdout, _) = gitproc.communicate()
    return stdout.strip()

def images_from_batch(xgen, rows=16, cols=16, order='bcwh'):

        I = np.round(255 * xgen).astype(np.float32)
        if order == 'bcwh':
            I = np.transpose(I, (0,2,3,1))
        bs = I.shape[0]
        im_rows = I.shape[1]
        im_cols = I.shape[2]
        im_channels = I.shape[3]
        im = np.zeros((rows*im_rows, cols*im_cols, im_channels))
        c = 0
        for i in range(rows):
            for j in range(cols):
                if c >= bs:
                    break
                im[i*im_rows:(i+1)*im_rows, j*im_cols:(j+1)*im_cols, :] = I[c,:,:,:]
                c = c + 1
        return im.astype(np.uint8)
