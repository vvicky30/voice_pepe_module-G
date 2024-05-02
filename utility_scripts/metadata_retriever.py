import importlib.metadata

def retrieve_metadata():
    try:
        # Retrieve metadata for the project
        project_metadata = importlib.metadata.metadata("voice_pepe")
        
        # Print the metadata
        print("Project metadata:")
        for key, value in project_metadata.items():
            print(f"{key}: {value}")
    except importlib.metadata.PackageNotFoundError:
        print("Package 'voice_pepe' not found.")

if __name__ == "__main__":
    retrieve_metadata()
