Issue: expression AST and validation.
Implemented AST nodes, recursive expression parsing, interpolation validation, matcher AST, and role/PAM caller validation.
Existing parse tests compile but older structural equality assertions fail because parsed expressions now retain AST nodes. Service/srv compilation is being checked with CGO disabled due to unavailable linux/hidraw.h.
