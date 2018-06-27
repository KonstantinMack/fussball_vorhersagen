
import pickle


def save_obj(obj, name):
    with open('C:/Users/Konny/DataScience/SpicedAcademy/fussball_vorhersagen/data/' + name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open('C:/Users/Konny/DataScience/SpicedAcademy/fussball_vorhersagen/data/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)
