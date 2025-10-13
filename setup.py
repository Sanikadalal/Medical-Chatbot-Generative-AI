from setuptools import find_packages, setup

setup(
    name="Generative AI Project",
    version="0.1.0",                    
    author="Sanika Dalal",
    author_email='sanikadalal3@gmail.com',
    packages=find_packages(),
    install_requires=[
        "sentence-transformers==2.2.2",
        "flask",
        "pypdf",
        "python-dotenv",
        "pinecone[grpc]",
        "langchain-pinecone",
        "langchain_community",
        "langchain_openai",
        "langchain_experimental",
     ]
)
