
class Message:
    """
    A message class which represents the message we sent. It includes all
    the information needed about the message- who sent it, who received it
    and what is the message.

    :ivar str sender: The name of the person who sent the message.
    :ivar str receiver: The name of the person who receive the message.
    :ivar str message: The message itself.
    :ivar bool opened: A variable that tells us if the user already opened the message or not yet.

    :param sender: The sender of the current message
    :param recipient: The recipient of the current message
    :param message: A string of the current message we want to send
    """
    def __init__(self, sender, recipient, message):
        self.message = message
        self.sender = sender
        self.recipient = recipient
        self.opened = False

    def __str__(self):
        return self.sender + ": " + self.message

    def __len__(self):
        return len(self.message)


class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message = Message(sender, recipient, message_body)
        if urgent:
            user_box.insert(0, message)
        else:
            user_box.append(message)
        return self.message_id

    def read_inbox(self, user_name: str, N = -1) -> list:
        """
        This function gets a username string that represents an inbox
        of a certain user, and an optional number that represents the amount
        of unread messages the user would like to get. The function will return
        a list of all the N unread messages that are waiting in the user's inbox.
        :param user_name: a string that represents a username's inbox.
        :param N: a number that represents the amount of unread messages to return.
        :return: a list of N unread messages in the user's inbox.
        """
        if N == -1 or N > len(self.boxes):
            N = self.message_id

        n_first_messages = []
        for message in range(0, N):
            if not self.boxes[user_name][message].opened:
                n_first_messages.append(self.boxes[user_name][message].__str__())
                self.boxes[user_name][message].opened = True

        return n_first_messages

    def search_inbox(self, user_name: str, string_to_search: str) -> list:
        """
        This function returns a list of all the messages that contain the string
        that the user passed.
        :param user_name: a string that represents a user's inbox.
        :param string_to_search: a string to search in the messages
        :return: a list of all messages in the inbox of user_name
        that contain the string string_to_search
        """
        all_messages_contain_the_string = [self.boxes[user_name][message].__str__() for message in
                                           range(0, self.message_id) if string_to_search in
                                           self.boxes[user_name][message].message or string_to_search in
                                           self.boxes[user_name][message].sender]
        return all_messages_contain_the_string


if __name__ == '__main__':
    inbox = PostOffice(["Adam"])
    inbox.send_message("Michal", "Adam", "Hello from Michal")
    inbox.send_message("Amit", "Adam", "Hello from Amit")
    print(inbox.read_inbox("Adam", 2))
    print(inbox.read_inbox("Adam", 2))
    print(inbox.search_inbox("Adam", "from"))
