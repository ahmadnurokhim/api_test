from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import random
import time
import numpy as np

app = Flask(__name__)
socketio = SocketIO(app)
maxDataPoints = 100
# Initialize the data points
data_points = [
    {'timestamp': 0, 'temperature': 1, 'humidity': 1},
    {'timestamp': 1, 'temperature': 0.9723066048468048, 'humidity': 1.108179983344208},
    {'timestamp': 2, 'temperature': 1.0584812056732233, 'humidity': 1.0173291403431872},
    {'timestamp': 3, 'temperature': 1.0943111678588489, 'humidity': 1.027310208835954},
    {'timestamp': 4, 'temperature': 1.0772590501056785, 'humidity': 0.9974222986509345},
    {'timestamp': 5, 'temperature': 0.9175697315775639, 'humidity': 0.9578940961575326},
    {'timestamp': 6, 'temperature': 0.6653249185778911, 'humidity': 0.8892262721400537},
    {'timestamp': 7, 'temperature': 0.7332774723771793, 'humidity': 0.9121575019257424},
    {'timestamp': 8, 'temperature': 0.6834663887769876, 'humidity': 1.0593586320446298},
    {'timestamp': 9, 'temperature': 0.6885249207184763, 'humidity': 1.2090397164897149},
    {'timestamp': 10, 'temperature': 0.6364331917914486, 'humidity': 1.2653204293023657},
    {'timestamp': 11, 'temperature': 0.7054310405299723, 'humidity': 1.4642486643082029},
    {'timestamp': 12, 'temperature': 0.5941966635098943, 'humidity': 1.4040023920413585},
    {'timestamp': 13, 'temperature': 0.6646683090703124, 'humidity': 1.1092751611161746},
    {'timestamp': 14, 'temperature': 0.584821723495883, 'humidity': 1.08479119390739},
    {'timestamp': 15, 'temperature': 0.6073701194939535, 'humidity': 1.016582077854653},
    {'timestamp': 16, 'temperature': 0.6172475096775913, 'humidity': 0.9247315780684944},
    {'timestamp': 17, 'temperature': 0.632587059385611, 'humidity': 0.8842435928439196},
    {'timestamp': 18, 'temperature': 0.5846074826825375, 'humidity': 0.6671815275000621},
    {'timestamp': 19, 'temperature': 0.5492658028589392, 'humidity': 0.7293328667403378},
    {'timestamp': 20, 'temperature': 0.548536262243072, 'humidity': 0.7875958709392374},
    {'timestamp': 21, 'temperature': 0.4861053021716077, 'humidity': 0.8880016810286617},
    {'timestamp': 22, 'temperature': 0.4743054392369743, 'humidity': 0.8761267318139871},
    {'timestamp': 23, 'temperature': 0.4689324827397062, 'humidity': 0.8655653107118562},
    {'timestamp': 24, 'temperature': 0.47132746547025584, 'humidity': 0.8604215204954492},
    {'timestamp': 25, 'temperature': 0.4709355123492029, 'humidity': 0.8529637988194644},
    {'timestamp': 26, 'temperature': 0.5268882824504947, 'humidity': 0.8693723322215976},
    {'timestamp': 27, 'temperature': 0.5641829198746624, 'humidity': 0.9425377233360465},
    {'timestamp': 28, 'temperature': 0.6410650595922853, 'humidity': 0.8969289046146699},
    {'timestamp': 29, 'temperature': 0.5815604337830094, 'humidity': 0.8722237865775353},
    {'timestamp': 30, 'temperature': 0.549477299994368, 'humidity': 0.8996067818705098},
    {'timestamp': 31, 'temperature': 0.5897410820883026, 'humidity': 0.6569084036705803},
    {'timestamp': 32, 'temperature': 0.6274237334181665, 'humidity': 0.5816502614324768},
    {'timestamp': 33, 'temperature': 0.5758064961635794, 'humidity': 0.674557561892356},
    {'timestamp': 34, 'temperature': 0.5361526618997998, 'humidity': 0.7039300621508358},
    {'timestamp': 35, 'temperature': 0.5078406789824005, 'humidity': 0.6456030820839951},
    {'timestamp': 36, 'temperature': 0.5091461551872046, 'humidity': 0.7655280827027454},
    {'timestamp': 37, 'temperature': 0.4708901641581681, 'humidity': 0.6932676746200676},
    {'timestamp': 38, 'temperature': 0.4454607883865048, 'humidity': 0.7216767731228514},
    {'timestamp': 39, 'temperature': 0.44241004936647466, 'humidity': 0.6687079816927158},
    {'timestamp': 40, 'temperature': 0.4255840140374849, 'humidity': 0.6446688017741271},
    {'timestamp': 41, 'temperature': 0.4354110644583058, 'humidity': 0.7740814723611454},
    {'timestamp': 42, 'temperature': 0.38257764596277766, 'humidity': 0.6786872797821367},
    {'timestamp': 43, 'temperature': 0.4134621029532046, 'humidity': 0.7171654363436252},
    {'timestamp': 44, 'temperature': 0.39594692055065256, 'humidity': 0.8013922109701954},
    {'timestamp': 45, 'temperature': 0.40047201433554463, 'humidity': 0.7939539182373604},
    {'timestamp': 46, 'temperature': 0.41295962346959747, 'humidity': 0.7038592961131671},
    {'timestamp': 47, 'temperature': 0.4056509402162018, 'humidity': 0.78924537099186},
    {'timestamp': 48, 'temperature': 0.44913970342534965, 'humidity': 0.6966429618892026},
    {'timestamp': 49, 'temperature': 0.399829361456048, 'humidity': 0.6847640071590951},
    {'timestamp': 50, 'temperature': 0.37483869876770176, 'humidity': 0.6637257433893335},
    {'timestamp': 51, 'temperature': 0.3496324631196495, 'humidity': 0.6178596608827068},
    {'timestamp': 52, 'temperature': 0.39374995555868036, 'humidity': 0.6552669180491418},
    {'timestamp': 53, 'temperature': 0.33128149393143475, 'humidity': 0.6838895368231983},
    {'timestamp': 54, 'temperature': 0.289627265855179, 'humidity': 0.5886026324489577},
    {'timestamp': 55, 'temperature': 0.3125253424831106, 'humidity': 0.6052113432891946},
    {'timestamp': 56, 'temperature': 0.34976842495688837, 'humidity': 0.6437692809945896},
    {'timestamp': 57, 'temperature': 0.34693208546594567, 'humidity': 0.7052945241779875},
    {'timestamp': 58, 'temperature': 0.3892369770497113, 'humidity': 0.5322356552931311},
    {'timestamp': 59, 'temperature': 0.41359711914058994, 'humidity': 0.4731359966457686},
    {'timestamp': 60, 'temperature': 0.38707359067242597, 'humidity': 0.38979747738428455},
    {'timestamp': 61, 'temperature': 0.3652014364253524, 'humidity': 0.31532807781738503},
    {'timestamp': 62, 'temperature': 0.36608318976613646, 'humidity': 0.2863991998381039},
    {'timestamp': 63, 'temperature': 0.3438061015641224, 'humidity': 0.26612643889512744},
    {'timestamp': 64, 'temperature': 0.3687885873390828, 'humidity': 0.2561770140700167},
    {'timestamp': 65, 'temperature': 0.34989192850925954, 'humidity': 0.2604347981182415},
    {'timestamp': 66, 'temperature': 0.3564835828528113, 'humidity': 0.19949141188276356},
    {'timestamp': 67, 'temperature': 0.3801626464298888, 'humidity': 0.18311459683619785},
    {'timestamp': 68, 'temperature': 0.3516804272745093, 'humidity': 0.207720610226011},
    {'timestamp': 69, 'temperature': 0.37373459230654027, 'humidity': 0.2204494792803385},
    {'timestamp': 70, 'temperature': 0.43297028326428877, 'humidity': 0.22765912798623142},
    {'timestamp': 71, 'temperature': 0.4100914727696458, 'humidity': 0.254668844874089},
    {'timestamp': 72, 'temperature': 0.3795339214447082, 'humidity': 0.2515151629191131},
    {'timestamp': 73, 'temperature': 0.36523593866219484, 'humidity': 0.24210572254250795},
    {'timestamp': 74, 'temperature': 0.313801290428105, 'humidity': 0.2518604007129472},
    {'timestamp': 75, 'temperature': 0.3350043547187241, 'humidity': 0.2571613388296165},
    {'timestamp': 76, 'temperature': 0.3087633585679668, 'humidity': 0.2292736634340204},
    {'timestamp': 77, 'temperature': 0.31951207469224674, 'humidity': 0.21712351028287066},
    {'timestamp': 78, 'temperature': 0.299719494311549, 'humidity': 0.19595314801048622},
    {'timestamp': 79, 'temperature': 0.2509408461032677, 'humidity': 0.1969594710517321},
    {'timestamp': 80, 'temperature': 0.24796188557281326, 'humidity': 0.192131167850924},
    {'timestamp': 81, 'temperature': 0.21527863455615773, 'humidity': 0.20981571837675436},
    {'timestamp': 82, 'temperature': 0.18251636575811225, 'humidity': 0.2009886095461025},
    {'timestamp': 83, 'temperature': 0.18723089901326853, 'humidity': 0.2122730664036817},
    {'timestamp': 84, 'temperature': 0.19567371685772747, 'humidity': 0.1828244774592447},
    {'timestamp': 85, 'temperature': 0.17833165026786754, 'humidity': 0.19142396621156157},
    {'timestamp': 86, 'temperature': 0.15628316867176473, 'humidity': 0.2113997649331368},
    {'timestamp': 87, 'temperature': 0.12897056199265033, 'humidity': 0.17908836282653096},
    {'timestamp': 88, 'temperature': 0.13688774208134893, 'humidity': 0.20269453086914593},
    {'timestamp': 89, 'temperature': 0.13467799410634762, 'humidity': 0.19888247579425386},
    {'timestamp': 90, 'temperature': 0.15081562225672998, 'humidity': 0.18654713509488308},
    {'timestamp': 91, 'temperature': 0.16316003822711692, 'humidity': 0.19280604178142471},
    {'timestamp': 92, 'temperature': 0.14932693642286848, 'humidity': 0.1784973603461036},
    {'timestamp': 93, 'temperature': 0.14334847735142162, 'humidity': 0.17877080197008477},
    {'timestamp': 94, 'temperature': 0.13328790876045135, 'humidity': 0.17716982104794135},
    {'timestamp': 95, 'temperature': 0.11718147534412857, 'humidity': 0.19157533235568372},
    {'timestamp': 96, 'temperature': 0.11361379890102787, 'humidity': 0.19889892727843173},
    {'timestamp': 97, 'temperature': 0.10527877986686555, 'humidity': 0.2057252920794012},
    {'timestamp': 98, 'temperature': 0.13678480803108067, 'humidity': 0.18227665993263592},
    {'timestamp': 99, 'temperature': 0.12947992298675304, 'humidity': 0.15886591919689932},
    {'timestamp': 100, 'temperature': 0.1262300154911254, 'humidity': 0.14385107659895724},
]

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/hi')
def hi():
    return "HALOOOOOOOOOOOOOOOOOOOO"

@socketio.on('initial_data_request')
def send_initial_data():
    emit('initial_data', data_points, namespace='/')

def update_data():
    while True:
        timestamp = time.strftime('%H:%M:%S')
        temperature = data_points[-1]['temperature'] * np.random.normal(1, 0.1)
        humidity = data_points[-1]['humidity'] * np.random.normal(1, 0.1)

        data_point = {'timestamp': timestamp, 'temperature': temperature, 'humidity': humidity}
        data_points.append(data_point)

        if len(data_points) > maxDataPoints:
            data_points.pop(0)

        socketio.emit('update_data', data_point, namespace='/')

        time.sleep(0.5)

if __name__ == '__main__':
    socketio.start_background_task(update_data)
    socketio.run(app)
