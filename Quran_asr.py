from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

class speech_recognition(Resource):

  def transcrip(filename = '/content/112.wav'):
    apikey = 'Se6YE35CW79ojYoojz3JjucUc2mhKhuBZCDBcEHRy6RS'
    url = 'https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/819a4f8d-c2a2-4bbf-ac65-5ac31ea5f603'

    authenticator = IAMAuthenticator(apikey)
    speech_to_text = SpeechToTextV1(
        authenticator=authenticator
    )

    speech_to_text.set_service_url(url)

    with open(join(dirname('__file__'), './.', filename),
                  'rb') as audio_file:
        speech_recognition_results = speech_to_text.recognize(
            audio=audio_file,
            content_type='audio/wav',
            model='ar-AR_BroadbandModel',
            word_confidence='true',
        ).get_result()
    return  speech_recognition_results['results']

  def get(self, wavfile):
    if (wavfile.lower().endswith('.wav')):
      return transcrip(wavfile), 200
    else:
      return "file should be wav", 404


# Setup the Api resource routing here
# Route the URL to the resource
api.add_resource(speech_recognition, '/')


if __name__ == '__main__':
    app.run(debug=True)

