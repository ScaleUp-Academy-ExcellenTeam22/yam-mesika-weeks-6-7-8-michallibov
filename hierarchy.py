
class User:
    """
    This class represents a user's information.
    It contains a username (string), password (string) and user_type(string).

    :ivar string username: Represents the username of the current user.
    :ivar string password: Represents the password of the current user.
    :ivar string user_type: Represents the type of the current user. It can be either a "Administrator" or "Regular".
    """
    def __init__(self, username: str, password: str, user_type: str):
        """
        A constructor.
        :param username: The username of the user we want to create.
        :param password: The password of the user we want to create.
        :param user_type: The type of the user we want to create.
        """
        self.username = username
        self.password = password
        self.user_type = user_type


class File:
    """
    The base class for all the types of the files- folder, text file or binary file.
    :ivar string file_type: The type of the file. It can be "Folder" or "Text" or "Binary"
    """
    def __init__(self, file_type: str):
        """
        A constructor.
        :param file_type: The type of the file we want to create.
        """
        self.file_type = file_type


class BinaryOrTextFile(File):
    """
    This class is a base class of the binary file and the text file.
    :ivar string file_type: Represents the type of the file.
    :ivar User user: Represents the user who created the current file.
    :ivar kb: Represents the size of the file in kilobytes.
    :ivar string content: Represents the content of the file.
    """
    def __init__(self, file_type: str, user: User, kb: int, content: str):
        """
        A constructor.
        :param file_type: The type of the current file we're creating.
        :param user: The user who created the current file.
        :param kb: The size in kb of the current file.
        :param content: The content of the current file.
        """
        super().__init__(file_type)
        self.kb = kb
        self.content = content
        self.user = user

    def read(self, user: User) -> str or None:
        """
        This function returns the content of the file if the user is the Administrator of the user who created
        this file, or None if the user is not the same user and not the Administrator.
        :param user: The user who wants to open and see the content of the current file.
        :return: The content (string) if the user is the Administrator or the same user who created the file,
        or None if not.
        """
        if (user.username == self.user.username and user.password == self.user.password) or \
                user.user_type == "Administrator":
            return self.content
        else:
            return None


class Folder(File):
    """
    The class that represents folder. It contains a list of files which allows it to save another
    files and folders inside of it.
    :ivar list files: A list of files.
    """
    def __init__(self):
        """
        A constructor.
        """
        super().__init__("Folder")
        self.files = []

    def add_file(self, file: File):
        """
        This function adds a file to the folder
        :param file: The file we want to add to the folder.
        :return: No return value
        """
        self.files.append(file)


class TextFile(BinaryOrTextFile):
    """
    A class that represents a text file.
    """
    def __init__(self, user: User, kb: int, content: str):
        """
        A constructor.
        :param user: The user who created the current file.
        :param kb: Represents the size of the file in kilobytes.
        :param content: Represents the content of the current file.
        """
        super().__init__("Text", user, kb, content)

    def count(self, string_to_search: str) -> int:
        """
        This function gets a string to search in the content of the file and returns
        how many times this string appears in the content of the file.
        :param string_to_search: A string that we want to count it's appearances in the file's content.
        :return: The amount of the appearances of the string string_to_search in the content of the file.
        """
        return self.content.count(string_to_search)


class BinaryFile(BinaryOrTextFile):
    """
    A class that represents a binary file.
    """
    def __init__(self, user: User, kb: int, content: str):
        """
         A constructor.
        :param user: The user who created the current file.
        :param kb: Represents the size of the file in kilobytes.
        :param content: Represents the content of the current file.
        """
        super().__init__("Binary", user, kb, content)

    def get_dimensions(self) -> None or set:
        """
        This function checks if the content of the binary file is image. If so,
        it will return the dimensions of the image that is in this file. Else,
        it will return None.
        :return: Dimensions of the image that is inside the current file if the
        content of the file is image, or None if the content of the file is not image.
        Note that in the exercise we didn't have to actually do all these calculations so
        I didn't return the dimensions.
        """
        if self.content != "Image":
            return None

        # Return dimensions set
        return


if __name__ == '__main__':
    new_folder = Folder()
    user_michal = User("Michal", "12345678", "Regular")
    user_asher = User("Asher", "87654321", "Regular")
    domain_user = User("Lea", "24687531", "Administrator")
    my_text_file = TextFile(user_asher, 15, "Hello, my name is Asher. I love my dog and my family.")
    new_folder.add_file(my_text_file)
    print(my_text_file.read(user_michal))
    print(my_text_file.read(user_asher))
    print(my_text_file.read(domain_user))
    print(my_text_file.count("my"))
