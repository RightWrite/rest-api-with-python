from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Pet(BaseModel):
    name: str
    category: str


pets = []


@app.get("/", summary="Welcome", description="Welcome to the Pet Store")
def hello():
    """
    Welcome to the Pet Store.

    This endpoint provides a welcome message for users.
    """
    return {"message": "Welcome to the Pet Store"}


@app.post("/pets", response_model=Pet, summary="Create Pet", description="Create a new pet")
def create_pet(pet: Pet):
    """
    Create a new pet.

    This endpoint allows you to create a new pet by providing its name and category.

    :param pet: The details of the pet to be created.
    :return: The created pet's details.
    """
    pets.append(pet)
    return pet


@app.get("/pets", response_model=list[Pet], summary="List Pets", description="Get a list of all pets")
def read_pets():
    """
    Get a list of all pets.

    This endpoint returns a list of all pets currently available in the store.

    :return: A list of pets.
    """
    return pets


@app.get("/pets/{pet_id}", response_model=Pet, summary="Read Pet", description="Get details of a specific pet by ID")
def read_pet(pet_id: int):
    """
    Get details of a specific pet by ID.

    This endpoint allows you to retrieve the details of a specific pet by providing its ID.

    :param pet_id: The ID of the pet to retrieve.
    :return: The details of the specified pet.
    :raises HTTPException 404: If the pet with the specified ID is not found.
    """
    if pet_id < 0 or pet_id >= len(pets):
        raise HTTPException(status_code=404, detail="Pet not found")
    return pets[pet_id]


@app.put("/pets/{pet_id}", response_model=Pet, summary="Update Pet", description="Update a pet by ID")
def update_pet(pet_id: int, pet: Pet):
    """
    Update a pet by ID.

    This endpoint allows you to update the details of a specific pet by providing its ID.

    :param pet_id: The ID of the pet to update.
    :param pet: The updated details of the pet.
    :return: The updated details of the pet.
    :raises HTTPException 404: If the pet with the specified ID is not found.
    """
    if pet_id < 0 or pet_id >= len(pets):
        raise HTTPException(status_code=404, detail="Pet not found")
    pets[pet_id] = pet
    return pet


@app.delete("/pets/{pet_id}", response_model=Pet, summary="Delete Pet", description="Delete a pet by ID")
def delete_pet(pet_id: int):
    """
    Delete a pet by ID.

    This endpoint allows you to delete a specific pet by providing its ID.

    :param pet_id: The ID of the pet to delete.
    :return: The details of the deleted pet.
    :raises HTTPException 404: If the pet with the specified ID is not found.
    """
    if pet_id < 0 or pet_id >= len(pets):
        raise HTTPException(status_code=404, detail="Pet not found")
    deleted_pet = pets.pop(pet_id)
    return deleted_pet
