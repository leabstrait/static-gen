config = {
    "title": "Projects",
    "description": "Explore our portfolio of projects.",
    "template": "projects/index.html",
    "categories": [
        {
            "name": "Commercial Projects",
            "projects": [
                {
                    "name": "Project 1",
                    "description": "Description of Project 1.",
                    "image": "/projects/commercial/project1/image.jpg",
                    "url": "/projects/commercial/project1",
                },
                {
                    "name": "Project 2",
                    "description": "Description of Project 2.",
                    "image": "/projects/commercial/project2/image.jpg",
                    "url": "/projects/commercial/project2",
                },
                # Additional projects in this category...
            ],
        },
        {
            "name": "Residential Projects",
            "projects": [
                {
                    "name": "Project 3",
                    "description": "Description of Project 3.",
                    "image": "/projects/residential/project3/image.jpg",
                    "url": "/projects/residential/project3",
                },
                {
                    "name": "Project 4",
                    "description": "Description of Project 4.",
                    "image": "/projects/residential/project4/image.jpg",
                    "url": "/projects/residential/project4",
                },
                # Additional projects in this category...
            ],
        },
        # Additional categories...
    ],
    "content": """
    [% markdown
    # Projects
    Explore our portfolio of projects.
    %]
    """,
}
