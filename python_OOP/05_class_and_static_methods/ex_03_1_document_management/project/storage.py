class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = next((c for c in self.categories if c.id == category_id), None)
        if category:
            category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = next((t for t in self.topics if t.id == topic_id), None)
        if topic:
            topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = next((d for d in self.documents if d.id == document_id), None)
        if document:
            document.edit(new_file_name)

    def delete_category(self, category_id: int):
        self.categories = [c for c in self.categories if c.id != category_id]

    def delete_topic(self, topic_id: int):
        self.topics = [t for t in self.topics if t.id != topic_id]

    def delete_document(self, document_id: int):
        self.documents = [d for d in self.documents if d.id != document_id]

    def get_document(self, document_id: int):
        return next((d for d in self.documents if d.id == document_id), None)

    def __repr__(self):
        return "\n".join(str(document) for document in self.documents)