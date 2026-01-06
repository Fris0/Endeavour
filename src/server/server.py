from fastapi import FastAPI
from fastmcp import FastMCP
from fastapi.encoders import jsonable_encoder
import requests
import json

api = "https://pokeapi.co/api/v2/"
mcp = FastMCP()

@mcp.tool()
def get_berry(name: str):
    """
    This tool returns information about the following:

    Get general information about specific berry.
    """
    response = requests.get(f"{api}berry/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_berry_firmness(name: str):
    """
    This tool returns information about the following:

    Get information about a berry its firmness.
    """
    response = requests.get(f"{api}berry-firmness/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_berry_flavor(name: str):
    """
    This tool returns information about the following:

    Get information about a berry its flavor.
    """
    response = requests.get(f"{api}berry-flavor/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_contest_type(name: str):
    """
    This tool returns information about the following:

    Get information about a contest.
    """
    response = requests.get(f"{api}contest-type/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_contest_effect(name: str):
    """
    This tool returns information about the following:

    Get information about a contest and the effect gives.
    """
    response = requests.get(f"{api}contest-effect/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_encounter_method(name: str):
    """
    This tool returns information about the following:

    Methods by which the player might can encounter Pokémon in the
    wild, e.g., walking in tall grass. 
    """
    response = requests.get(f"{api}encounter-method/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_encounter_condition(name: str):
    """
    This tool returns information about the following:

    Conditions which affect what pokemon
    might appear in the wild, e.g., day or night.
    """
    response = requests.get(f"{api}sencounter-condition/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_evolution_chain(name: str):
    """
    This tool returns information about the following:

    Tool that returns the following type of information:
    Evolution chains are essentially family trees. They start with the lowest stage within a family
    and detail evolution conditions for each as well as Pokémon they can evolve into up through the hierarchy.

    requires evolutions id and not pokemon name.
    """

    response = requests.get(f"{api}pokemon/{name.lower()}")
    id = response.json()["id"]

    response = requests.get(f"{api}evolution-chain/{id}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_generation(name: str):
    """
    This tool returns information about the following:

    A generation is a grouping of the Pokémon games that separates them based on the Pokémon they include.
    In each generation, a new set of Pokémon, Moves, Abilities and Types that did not exist in the previous
    generation are released.
    """
    response = requests.get(f"{api}generation/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_pokedex(name: str):
    """
    This tool returns information about the following:

    A Pokédex is a handheld electronic encyclopedia device;
    one which is capable of recording and retaining information of the various Pokémon in a given region-
    with the exception of the national dex and some smaller dexes related to portions of a region.
    """
    response = requests.get(f"{api}pokedex/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_item(name: str):
    """
    This tool returns information about the following:

    An item, which is an object in the games which the player can pick up, keep in their bag,
    and use in some manner. They have various uses, including healing,
    powering up, helping catch Pokémon, or to access a new area.
    """
    response = requests.get(f"{api}item/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_item_attribute(name: str):
    """
    This tool returns information about the following:

    Item attributes define particular aspects of items, e.g. "usable in battle" or "consumable".
    """
    response = requests.get(f"{api}item-attribute/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_item_category(name: str):
    """
    This tool returns information about the following:

    Item categories determine where items will be placed in the players bag.
    """
    response = requests.get(f"{api}item-category/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_item_fling_effect(name: str):
    """
    This tool returns information about the following:

    The various effects of the move "Fling" when used with different items.
    """
    response = requests.get(f"{api}super-contest-effect/{name.lower()}")
    data = response.json()
    return jsonable_encoder(data)

@mcp.tool()
def get_item_pocket(name: str):
    """
    This tool returns information about the following:

    Pockets within the players bag used for storing items by category.
    """
    response = requests.get(f"{api}item-pocket/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_location(name: str):
    """
    This tool returns information about the following:

    Locations that can be visited within the games.
    Locations make up sizable portions of regions, like cities or routes.
    """
    response = requests.get(f"{api}location/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_location_area(name: str):
    """
    This tool returns information about the following:

    Location areas are sections of areas, such as floors in a building or cave.
    Each area has its own set of possible Pokémon encounters.

    """
    response = requests.get(f"{api}location-area/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_region(name: str):
    """
    This tool returns information about the following:

    A region is an organized area of the Pokémon world. Most often,
    the main difference between regions is the species of Pokémon that can be encountered within them.

    """
    response = requests.get(f"{api}region/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_machine(name: str):
    """
    This tool returns information about the following:

    Machines are the representation of items that teach moves to Pokémon.
    They vary from version to version, so it is not certain that one specific TM or HM corresponds to a single Machine.

    """
    response = requests.get(f"{api}machine/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_move(name: str):
    """
    This tool returns information about the following:

    Moves are the skills of Pokémon in battle. In battle, a Pokémon uses one move each turn.
    Some moves (including those learned by Hidden Machine) can be used outside of battle as well,
    usually for the purpose of removing obstacles or exploring new areas.
    """
    response = requests.get(f"{api}move/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_pokemon(name: str):
    """
    This tool returns information about the following:

    Pokémon are the creatures that inhabit the world of the Pokémon games.
    They can be caught using Pokéballs and trained by battling with other Pokémon. 
    each Pokémon belongs to a specific species but may take on a variant which makes
    it differ from other Pokémon of the same species, such as base stats, available abilities and typings.
    """
    response = requests.get(f"{api}pokemon/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

mcp_app = mcp.http_app(path='/mcp')
app = FastAPI(title="Pokemon API", lifespan=mcp_app.lifespan)
app.mount("/api", mcp_app)

@app.get("/")
async def root():
    return {"Server": "OK"}