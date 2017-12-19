# -*- coding: iso-latin-1 -*-
#=============================================================================

__license__ = "https://raw.githubusercontent.com/20Tauri/DoxyDoxygen_contrib_HeaderDoc/master/LICENSE.md"


#-----------------------------------------------------------------------------
## @brief      HeaderDoc commands description
##
COMMANDS_LIST = [
    DoxyCommand( '@const',            '\t{ description_of_the_variable }',                              help = "Documents a constant within an enumeration", aliases = [ '@constant' ]),
    DoxyCommand( '@param',            '\t<parameter_name>\t{ parameter_description }', key_index = 0,   help = "Documents the parameter to a function"),
    DoxyCommand( '@return',           '\t{ description_of_the_return_value }',                          help = "Documents the return value of a function", aliases = [ '@results' ]),
    DoxyCommand( '@throws',           '\t<exception_object>\t{ exception_description }', key_index = 0, help = "Starts an exception description for an exception object with name <exception-object>"),
    DoxyCommand( '@var',              '\t{ description_of_the_variable }',                              help = "Documents a local variable in a function or method"),
]

#-----------------------------------------------------------------------------
## @brief      This class describles the specific style of documentation used
##             in HeaderDoc
##
## @see        HeaderDoc Tutorial <https://www.raywenderlich.com/66395/documenting-in-xcode-with-headerdoc-tutorial>
##
class DocStyle(DocStyleBase):
    ## Name of this style (will be used in your `profiles` settings)
    name = "HeaderDoc"

    #-------------------------------------------------------------------------
    ## @brief      The constructor
    ##
    ##             It will define the list of availables commands.
    ##             This list will be used for completion, formating...
    ##
    ##             A command is composed in:
    ##                - A name
    ##                - An arguments format string
    ##                      - If <sharp> braces are used the argument is a single word.
    ##                      - If (round) braces are used the argument extends until the end of
    ##                        the line on which the command was found.
    ##                      - If {curly} braces are used the argument extends until the next
    ##                        paragraph. Paragraphs are delimited by a blank line or by a
    ##                        section indicator.
    ##                      - And [] mark in optional block
    ##                - An optional `key_index` is o,e argument is a key (0 is first)
    ##                - An optional `help` string to give to command description
    ##                - An optional `aliases` list that give the name of aliases
    ##
    ## @param      self  The DocStyle object
    ##
    def __init__(self):
        DocStyleBase.__init__(self, COMMANDS_LIST)

    #-------------------------------------------------------------------------
    ## @brief      Build the commands list tht match a definition
    ##
    ## @param      self        The object
    ## @param      definition  The definition
    ##
    ## @return     The generated commands list.
    ##
    def definition_to_commands_list(self, definition):
        commands_list = []

        if definition["kind"] in ["var"]:
            commands_list += self.command("@var")
        elif definition["kind"] in [ "constant" ]:
            commands_list += self.command("@const")
        else:
            for param in definition["params"]:
                commands_list += self.command("@param", [ param.name ])

            definition_return = definition["return"]
            if definition_return and definition_return != "void":
                commands_list += self.command("@return")

            for type_name in definition["throws"]:
                commands_list += self.command("@throws", [ type_name ])

        return commands_list

    #-------------------------------------------------------------------------
    ## @brief      Returns the list of commands that can be generate.
    ##
    ##             Generable commands are remove from `layout` when missing.
    ##
    ## @param      self  The object
    ##
    ## @return     The list
    ##
    def generable_commands_names(self):
        return [
            "@var",
            "@const",
            "@param",
            "@return",
            "@throws",
        ]
