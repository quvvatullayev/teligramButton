import json, requests
import pstats

TOKIN = '5505244566:AAFRwoxaYH-ahK27OKN0_6MPKStev9LJ1R4'

def teligramButton(chat_id:int):
    buttomTxet1 = {'text':'👫Pley With Frends'}
    buttomTxet2 = {'text':'🔥Trending gemes'}
    buttomTxet3 = {'text':'⏱Last Pley gemes'}
    buttomTxet4 = {'text':'🎮Categories'}
    buttomTxet5 = {'text':'🚀jain GAMME Toking Channal'}
    buttomTxet6 = {'text':'💰Get App & Wen Cash'}

    reply_markup = {
        'keyboard' : [
        [buttomTxet1, buttomTxet2],
        [buttomTxet3, buttomTxet4],
        [buttomTxet5, buttomTxet6]
        ]}
    data = {'chat_id':chat_id, 'text':'test', 'reply_markup':reply_markup}
    url = f'https://api.telegram.org/bot{TOKIN}/sendMessage'
    data = requests.get(url, json=data)
    return data.json()
teligramButton(677038439)
