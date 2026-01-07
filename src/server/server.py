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
    Fetch detailed information about a specific Pokémon berry.

    Use this tool when you need structured data about a berry, including
    its size, growth time, firmness, flavors, and effects.

    Args:
        name (str): The berry name or numeric ID
                    (e.g. "cheri", "pecha", "1"). Case-insensitive and
                    must match PokéAPI identifiers.

    Returns:    
        dict: A JSON object from the PokéAPI containing berry data, including:
              - Berry name
              - Growth time
              - Size and smoothness
              - Firmness
              - Flavors and potency
              - Natural effects
    """

    response = requests.get(f"{api}berry/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_berry_firmness(name: str):
    """
    Fetch information about a Pokémon berry’s firmness.

    Use this tool when you need details about a berry’s firmness, such as
    how hard or soft it is and which berries share the same firmness.

    Args:
        name (str): The berry firmness name or numeric ID
                    (e.g. "soft", "very-hard", "1"). Case-insensitive and
                    must match PokéAPI identifiers.

    Returns:
        dict: A JSON object from the PokéAPI containing berry firmness data,
              including the firmness name, description, and berries that
              have this firmness.
    """
    response = requests.get(f"{api}berry-firmness/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_berry_flavor(name: str):
    """
    Fetch information about a Pokémon berry flavor.

    Use this tool when you need details about a berry’s flavor, such as
    how it affects Pokémon contest attributes or taste preferences.

    Args:
        name (str): The berry flavor name or numeric ID
                    (e.g. "spicy", "sweet", "1"). Case-insensitive and must
                    match PokéAPI identifiers.

    Returns:
        dict: A JSON object from the PokéAPI containing berry flavor data,
              including the flavor name, associated contest type, and
              berries that have this flavor.
    """
    response = requests.get(f"{api}berry-flavor/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_contest_type(name: str):
    """
    Fetch information about a Pokémon contest type.

    Use this tool when you need details about a contest type, such as
    its name, associated appeal, jam values, and related moves.

    Args:
        name (str): The contest type name or numeric ID
                    (e.g. "cool", "cute", "1"). Case-insensitive and must
                    match PokéAPI identifiers.

    Returns:
        dict: A JSON object from the PokéAPI containing contest type data,
              including the type name, effects on contest scoring, and
              associated moves.
    """
    response = requests.get(f"{api}contest-type/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_contest_effect(name: str):
    """
    Fetch information about a Pokémon contest effect.

    Use this tool when you need details about the effect of a move or
    action in a Pokémon contest, such as the impact on contest stats
    or judge scoring.

    Args:
        name (str): The contest effect name or numeric ID
                    (e.g. "1", "2"). Case-insensitive and must match
                    PokéAPI identifiers.

    Returns:
        dict: A JSON object from the PokéAPI containing contest effect data,
              including effect descriptions and related moves or actions.
    """
    response = requests.get(f"{api}contest-effect/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_encounter_method(name: str):
    """
    Fetch information about a Pokémon encounter method.

    Use this tool when you need to know how a Pokémon can be encountered
    in the wild, such as walking in tall grass, fishing, or using special
    items.

    Args:
        name (str): The encounter method name or numeric ID
                    (e.g. "walk", "surf", "fishing-rod", "1").
                    Case-insensitive and must match PokéAPI identifiers.

    Returns:
        dict: A JSON object from the PokéAPI containing encounter method data,
              including the method name, description, and related encounter
              details.
    """
    response = requests.get(f"{api}encounter-method/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_encounter_condition(name: str):
    """
    Fetch information about a Pokémon encounter condition.

    Use this tool when you need to know the factors that affect which
    Pokémon appear in the wild, such as time of day, weather, or other
    environmental conditions.

    Args:
        name (str): The encounter condition name or numeric ID
                    (e.g. "time-of-day", "weather", "1").
                    Case-insensitive and must match PokéAPI identifiers.

    Returns:
        dict: A JSON object from the PokéAPI containing encounter condition
              data, including the condition name, description, and possible
              values that influence wild Pokémon appearances.
    """
    response = requests.get(f"{api}sencounter-condition/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_evolution_chain(name: str):
    """
    Fetch the evolution chain for a Pokémon.

    Use this tool when you need to know how a Pokémon evolves, including
    its full evolution family and the conditions required for each
    evolution step.

    Args:
        name (str): The Pokémon name or numeric Pokédex ID
                    (e.g. "eevee", "pikachu", "133").
                    Case-insensitive.

    Returns:
        dict: A JSON object from the PokéAPI describing the evolution chain,
              including all species in the chain and the conditions under
              which each evolution occurs.
    """

    response = requests.get(f"{api}pokemon/{name.lower()}")
    id = response.json()["id"]

    response = requests.get(f"{api}evolution-chain/{id}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_generation(name: str):
    """
    Fetch information about a Pokémon game generation.

    Use this tool when you need data about a specific generation of Pokémon
    games, such as which Pokémon, moves, abilities, and types were introduced.

    Args:
        name (str): The generation name or numeric ID
                    (e.g. "generation-i", "generation-iii", "3").
                    Case-insensitive and must match PokéAPI identifiers.

    Returns:
        dict: A JSON object from the PokéAPI containing generation data,
            including introduced Pokémon species, moves, abilities, types,
            and associated regions.
    """
    response = requests.get(f"{api}generation/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_pokedex(name: str):
    """
    Fetch information about a specific Pokédex.

    Use this tool when you need data about a regional or special Pokédex,
    such as which Pokémon entries it contains or which region it is
    associated with.

    Args:
        name (str): The Pokédex name or numeric ID
                    (e.g. "kanto", "national", "2").
                    Case-insensitive and must match PokéAPI identifiers.

    Returns:
        dict: A JSON object from the PokéAPI containing Pokédex data,
              including the region, descriptions, and Pokémon entries
              listed in that Pokédex.
    """
    response = requests.get(f"{api}pokedex/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_item(name: str):
    """
    Fetch detailed information about a Pokémon item.

    Use this tool when you need structured data about an item’s effects,
    category, attributes, or in-game usage.

    Args:
        name (str): The item name or numeric ID
                    (e.g. "potion", "master-ball", "1").
                    Case-insensitive and must match PokéAPI identifiers.

    Returns:
        dict: A JSON object from the PokéAPI containing item data such as
              effect text, category, attributes, fling effect, and cost.
    """
    response = requests.get(f"{api}item/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_item_attribute(name: str):
    """
    Fetch information about a Pokémon item attribute.

    Use this tool to understand special properties that items can have,
    such as whether an item is consumable, usable in battle, or usable
    outside of battle.

    Args:
        name (str): The item attribute name or numeric ID
                    (e.g. "consumable", "usable-in-battle", "1").
                    Case-insensitive and must match PokéAPI identifiers.

    Returns:
        dict: A JSON object from the PokéAPI containing item attribute data,
              including the attribute description and the items that have
              this attribute.
    """
    response = requests.get(f"{api}item-attribute/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_item_category(name: str):
    """
    Fetch information about a Pokémon item category.

    Use this tool when you need to know how items are grouped in the
    player's bag (e.g. medicine, berries, key items).

    Args:
        name (str): The item category name or numeric ID
                    (e.g. "medicine", "berries", "1").
                    Case-insensitive and must match PokéAPI identifiers.

    Returns:
        dict: A JSON object from the PokéAPI containing item category data,
              including the category name and the items that belong to it.
    """
    response = requests.get(f"{api}item-category/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_item_fling_effect(name: str):
    """
    Fetch information about the effect of the move "Fling" when used with a
    specific item.

    Use this tool when you need to know what additional effect an item
    causes if it is thrown using the move Fling.

    Args:
        name (str): The item or fling-effect identifier (e.g. "toxic-orb",
                    "iron-ball"). Case-insensitive and must match PokéAPI
                    identifiers.

    Returns:
        dict: A JSON object from the PokéAPI describing the fling effect,
              including effect text and related items.
    """
    response = requests.get(f"{api}item-fling-effect/{name.lower()}")
    data = response.json()
    return jsonable_encoder(data)

@mcp.tool()
def get_location(name: str):
    """
    Fetch detailed information about a Pokémon game location by name or ID.

    Args:
        name (str): The location name or numeric ID (e.g. "kanto-route-1",
                    "viridian-city", "1"). Case-insensitive and should match
                    PokéAPI location identifiers.

    Returns:
        dict: A JSON object from the PokéAPI containing location data such as
              region, areas within the location, and game version details.
    """
    response = requests.get(f"{api}location/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_location_area(name: str):
    """
    Fetch detailed information a location area. Including a list of methods a pokemon may
    be encoutered and a list of pokemons that can be encountered.

    Args:
        name (str): Name of area or numeric id (e.g. location area written as "canalave-city-area" or its numeric value "1")
    
    Output:
        dict: A JSON object from the PokeAPI containing information about 
        pokemons that can be encountered, how they can be encountered and name of town
        or its corresponding id.
    """
    response = requests.get(f"{api}location-area/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_region(name: str):
    """
    Fetch detailed information about a region and pokedexes that catalogue pokemon in
    given region.

    Args:
        name (str): Name of region or numeric id (e.g. "kanto")
    
    Output:
        dict: A JSON object from the PokeAPI containing information about 
        if the machine is HM or TM and the move it teaches.
    """
    response = requests.get(f"{api}region/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_machine(name: str):
    """
    Fetch detailed information about a machine and the move it teaches to a pokemon.

    Args:
        name (str): Numeric ID of machine (e.g. 1)
    
    Output:
        dict: A JSON object from the PokeAPI containing information about 
        if the machine is HM or TM and the move it teaches.

    """
    response = requests.get(f"{api}machine/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_move(name: str):
    """
    Fetch detailed information about a Pokémon move by name.

    Args:
        name (str): The name of the Pokémon move (e.g. "thunderbolt", "ice-beam").
                    The name is case-insensitive.

    Returns:
        dict: A JSON object from the PokéAPI containing move details such as
              power, accuracy, PP, type, damage class, and effect text.
    """
    response = requests.get(f"{api}move/{name.lower()}")
    data = response.json()

    return jsonable_encoder(data)

@mcp.tool()
def get_pokemon(name: str):
    """
    Fetch detailed information about a Pokémon by name or ID.

    Args:
        name (str): The Pokémon name or numeric ID (e.g. "pikachu", "charizard", "25").
                    The value is case-insensitive.

    Returns:
        dict: A JSON object from the PokéAPI containing Pokémon data such as
              base stats, types, abilities, forms/variants, sprites, and height/weight.
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