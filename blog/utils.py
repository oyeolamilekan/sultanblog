def mentee_sender(post,mentee):
    reciever_list = []
    from_email = 'johnsonoye34@gmail.com'
    subject = post.title
    message = post.body[0:240]
    for ment in mentee:
      reciever_list.append(ment.email_field)
    print(reciever_list)
    print('kk')