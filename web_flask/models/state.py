from models import storage
from models.city import City

class State(BaseModel, Base):
    if models.storage_t != 'db':
        @property
        def cities(self):
            """
            Returns the list of City instances with state_id equals to the current State.id
            """
            all_cities = storage.all(City)
            state_cities = [city for city in all_cities.values() if city.state_id == self.id]
            return state_cities
