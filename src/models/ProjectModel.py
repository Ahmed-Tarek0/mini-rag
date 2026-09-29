from .BaseDataModel import BaseDataModel
from .db_schemas import Project
from .enums.DataBaseEnum import DataBaseEnum


class ProjectModel(BaseDataModel):
    
    def __init__(self, db_client: object):
        super().__init__(db_client=db_client)
        self.collection = self.db_client[DataBaseEnum.COLLECTION_PROJECT_NAME.value]
        
    
    async def create_project(self, project: Project):
        # Create a new project in the database.

        result = await self.collection.insert_one(project.dict(by_alias=True, exclude_unset=True))
        project._id = result.inserted_id
        
        return project
    
    
    async def get_project_or_crate_one(self, project_id: str):
        # Get a project by its ID. If the project does not exist, create a new one.
 
        record = await self.collection.find_one({"project_id": project_id})
        
        if record is None:
            # create new project
            new_project = Project(project_id=project_id)
            new_project = await self.create_project(project=new_project)
            
            return new_project
        
        return Project(**record)
    
    
    async def get_all_projects(self, page: int = 1, page_size: int = 10):
        # Get all projects from the database.
        # Don't use get all without pagination.

        # count total number of documents in the collection
        total_documents = await self.collection.count_documents({})
        
        # calculate the total number of pages
        total_pages = total_documents // page_size
        if total_documents % page_size > 0:
            total_pages += 1

        cursor = self.collection.find().skip((page - 1) * page_size).limit(page_size)
        projects = [Project(**doc) async for doc in cursor]
        
        return projects, total_pages