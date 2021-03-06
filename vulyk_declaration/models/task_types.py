from vulyk.models.task_types import AbstractTaskType

from vulyk_declaration.models.tasks import DeclarationAnswer, DeclarationTask


class DeclarationTaskType(AbstractTaskType):
    """
    Declaration Task to work with Vulyk.
    """
    answer_model = DeclarationAnswer
    task_model = DeclarationTask

    template = "index.html"
    helptext_template = "help.html"
    type_name = "declaration_task"

    redundancy = 3

    JS_ASSETS = ["static/scripts/html5shiv.js",
                 "static/scripts/jquery-ui.min.js",
                 "static/scripts/jquery.validate.min.js",
                 "static/scripts/messages_uk.min.js",
                 "static/scripts/jquery-cloneya.min.js",
                 "static/scripts/jquery.dateSelectBoxes.js",
                 "static/scripts/jquery.placeholder.min.js",
                 "static/scripts/jquery.serializejson.js",
                 "static/scripts/main.js"]

    CSS_ASSETS = ["static/styles/core-style.css",
                  "static/styles/style.css"]
