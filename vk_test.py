import vk_api
import time


def main():
    session = vk_api.VkApi('89892829533', 'Zusehi66')
    try:
        session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = session.get_api()
    response = vk.users.get(user_ids='269633932', fields='online, last_seen')
    fields = {
        'online': response[0]['online'],
        'time': response[0]['last_seen']['time']
    }
    if fields['online']:
        print('Эта сука онлайн!')
    else:
        print('Оффлайн. Заходила в', time.ctime(fields['time']))
main()
