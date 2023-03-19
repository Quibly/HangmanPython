import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def createDatabase():
    # Use a service account.
    cred = credentials.Certificate('./game/data/hangman.json')
    app = firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db

db = createDatabase()

#call a database reference
class Database:
    def __init__(self):
        self.dataset = db

    # Method to add data to a collection
    def get_data(self, collection):
        if collection == 'users':
            reference = self.dataset.collection(u'users')
        elif collection == 'puzzles':
            reference = self.dataset.collection(u'puzzles')
        docs = reference.stream()
        return docs
        #for doc in docs:
        #    print(f'{doc.id} => {doc.to_dict()}')

    # Method to add data to a collection
    def add_data(self, collection, value=''):
        if collection == 'users':
            gamertag = value
            reference = self.dataset.collection(u'users').document()
            reference.set({
                u'gamertag': gamertag,
                u'rank': u'Beginner',
                U'puzzles': []
            })
        elif collection == 'puzzles':
            puzzle = input('Please enter the new puzzle string: ')
            reference = self.dataset.collection(u'puzzles').document()
            reference.set({
                u'puzzle': puzzle
            })

    # Method to change the gamertag of the user in the database
    def change_gamertag(self, existingGamertag, newGamertag):
        id = self.get_user(existingGamertag)
        self.dataset.collection(u'users').document(id).update({u'gamertag': newGamertag})

    # Method to update the puzzle history on gamer details in database
    def change_puzzles(self, gamertag, puzzle):
        gamerId = self.get_user(gamertag)
        docs = self.get_data('puzzles')
        for doc in docs:
            dictionary = doc.to_dict()
            p = dictionary['puzzle']
            if puzzle == p:
                puzzleId = doc.id
                gamer = self.dataset.collection(u'users').document(gamerId).get()
                gamerDict = gamer.to_dict()
                gamerpuzzles = gamerDict['puzzles']
                if gamerpuzzles == None:
                    self.dataset.collection(u'users').document(gamerId).update({u'puzzles': puzzleId})
                else:
                    self.dataset.collection(u'users').document(gamerId).update({u'puzzles': firestore.ArrayUnion([puzzleId])})

    # Method to delete user
    def delete_data(self, gamertag):
        id = self.get_user(gamertag)
        self.dataset.collection(u'users').document(id).delete()

    # Method to get user id
    def get_user(self, gamertag):
        docs = self.get_data('users')
        for doc in docs:
            dictionary = doc.to_dict()
            gt = dictionary['gamertag']
            if gt == gamertag:
                return doc.id


        