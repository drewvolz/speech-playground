import subprocess
import uuid
import glob


def say(voice, phrase):
    unique_id = str(uuid.uuid4())
    filename = f'{unique_id}.aiff'
    subprocess.run(['say', '-v', voice, phrase,  '-o', filename])
    print(f"file {filename}", file=open('input.txt', 'a'))


def generate_audio():
    say('Tom',  'papa, what was internet like when you were a boy?')
    say('Fred', 'EEEEEEEEEEEEEEEEEEEEEE')
    say('Fred', 'bwong bwong bwong')
    say('Tom',  'papa, are u ok')
    say('Fred', 'krrrrrrrrrrrrrrrrr')
    say('Fred', 'thumbnail')


def concat_audio():
    subprocess.run(['ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', 'input.txt', '-c', 'copy', 'output.aiff'])


def convert_audio():
    subprocess.run(['ffmpeg', '-y', '-i', 'output.aiff', '-f', 'mp3', 'output.mp3'])


def cleanup():
    subprocess.run(['rm', '-rf', 'input.txt'])
    subprocess.run(['rm'] + glob.glob('*.aiff'))


def main():
    generate_audio()
    concat_audio()
    convert_audio()
    cleanup()


if __name__ == '__main__':
    main()
