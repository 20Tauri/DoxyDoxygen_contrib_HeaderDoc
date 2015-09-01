# -*- encoding: iso-latin-1 -*-
#============================================================================
__license__ = "https://raw.githubusercontent.com/20Tauri/DoxyDoxygen_contrib_HeaderDoc/master/LICENSE.md"


if "DoxyCommand" in locals():
    #----------------------------------------------------------------------------
    ## @brief      HeaderDoc commands description
    ##
    ## @see        https://developer.apple.com/library/mac/documentation/DeveloperTools/Conceptual/HeaderDoc/tags/tags.html#//apple_ref/doc/uid/TP40001215-CH346-CHDJFEGF
    ##
    COMMANDS_LIST = [
        #
        # name:
        #   Name on the command
        #
        # args_format:
        #   If <sharp> braces are used the argument is a single word.
        #   If (round) braces are used the argument extends until the end of the line on which the command was found.
        #   If {curly} braces are used the argument extends until the next paragraph. Paragraphs are delimited by a blank line or by a section indicator.
        #   And [] mark in optional block
        #
        # key_index:
        #   If a parameter is a key, this position (firsty is 0)
        #
        # help:
        #   Command description
        #
        # aliases:
        #   List of aliases names for this commands
        #
        DoxyCommand( '@const',            '\t{ description_of_the_variable }',                              help = "Documents a constant within an enumeration", aliases = [ '@constant' ]),
        DoxyCommand( '@param',            '\t<parameter_name>\t{ parameter_description }', key_index = 0,   help = "Documents the parameter to a function"),
        DoxyCommand( '@return',           '\t{ description_of_the_return_value }',                          help = "Documents the return value of a function", aliases = [ '@results' ]),
        DoxyCommand( '@throws',           '\t<exception_object>\t{ exception_description }', key_index = 0, help = "Starts an exception description for an exception object with name <exception-object>"),
        DoxyCommand( '@var',              '\t{ description_of_the_variable }',                              help = "Documents a local variable in a function or method"),
    ]

    class DocStyle(DocStyleBase):
        name = "HeaderDoc"

        def __init__(self):
            DocStyleBase.__init__(self, COMMANDS_LIST)

        def generate_uncommented_text(self, definition):
            uncommented_text = ""

            if definition["kind"] in ["var"]:
                uncommented_text += self.command("@var", [])
            elif definition["kind"] in [ "constant" ]:
                uncommented_text += self.command("@const", [])
            else:
                for (_, _, name, _) in definition["params"]:
                    uncommented_text += self.command("@param", [ name ])

                definition_return = definition["return"]
                if definition_return and definition_return != "void":
                    uncommented_text += self.command("@return", [])

                for type_name in definition["throws"]:
                    uncommented_text += self.command("@throws", [ type_name ])

            return uncommented_text
