import sys
import messages
import fourier
import speechdetector

from recordaudio import AudioRecorder

# Variables pool

messageHelper = messages.MessageHelper()
arguments_no = len(sys.argv)
arguments = sys.argv
recorder = AudioRecorder()


# Methods pool
def handle_help():
    f = open('help.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()


# Script
messageHelper.welcome_message()

if arguments_no > 3:
    messageHelper.wrong_usage()
if arguments_no == 1:
    filename = recorder.record_audio()
    speechdetector.detect_from_file(filename)
    recorder.generate_plot(filename)
else:
    for index in range(len(arguments)):
        if arguments[index] == '-h':
            handle_help()
            break
        if arguments[index] == '-s':
            if index + 1 >= arguments_no:
                messageHelper.wrong_usage()
            else:
                filename = recorder.record_audio(seconds=int(arguments[index+1]))
                speechdetector.detect_from_file(filename)
                recorder.generate_plot(filename)
            break
        if arguments[index] == '-f':
            if index + 1 >= arguments_no:
                messageHelper.wrong_usage()
            else:
                fourier.calculate_fourier(arguments[index+1])
            break
