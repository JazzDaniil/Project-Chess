import pawn
import rook
import bishop


def get_save(request):
    board = ""
    if request == "new_save":
        board = [[{"00": ["rook", "figure", rook.Rook("black")]}, {"01": ["knight", "figure", pawn.Pawn("black")]},
                  {"02": ["bishop", "figure", bishop.Bishop("black")]}, {"03": ["queen", "figure", pawn.Pawn("black")]},
                  {"04": ["king", "figure", pawn.Pawn("black")]}, {"05": ["bishop", "figure", bishop.Bishop("black")]},
                  {"06": ["knight", "figure", pawn.Pawn("black")]}, {"07": ["rook", "figure", rook.Rook("black")]}],
                 [{"10": ["pawn", "figure", pawn.Pawn("black")]}, {"11": ["pawn", "figure", pawn.Pawn("black")]},
                  {"12": ["pawn", "figure", pawn.Pawn("black")]}, {"13": ["pawn", "figure", pawn.Pawn("black")]},
                  {"14": ["pawn", "figure", pawn.Pawn("black")]}, {"15": ["pawn", "figure", pawn.Pawn("black")]},
                  {"16": ["pawn", "figure", pawn.Pawn("black")]}, {"17": ["pawn", "figure", pawn.Pawn("black")]}],
                 [{"20": [None]}, {"21": [None]}, {"22": [None]}, {"23": [None]},
                  {"24": [None]}, {"25": [None]}, {"26": [None]}, {"27": [None]}],
                 [{"30": [None]}, {"31": [None]}, {"32": [None]}, {"33": [None]},
                  {"34": [None]}, {"35": [None]}, {"36": [None]}, {"37": [None]}],
                 [{"40": [None]}, {"41": [None]}, {"42": [None]}, {"43": [None]},
                  {"44": [None]}, {"45": [None]}, {"46": [None]}, {"47": [None]}],
                 [{"50": [None]}, {"51": [None]}, {"52": [None]}, {"53": [None]},
                  {"54": ["pawn", "figure", pawn.Pawn("white")]}, {"55": ["pawn", "figure", pawn.Pawn("black")]},
                  {"56": [None]}, {"57": [None]}],
                 [{"60": ["pawn", "figure", pawn.Pawn("white")]}, {"61": ["pawn", "figure", pawn.Pawn("white")]},
                  {"62": ["pawn", "figure", pawn.Pawn("white")]}, {"63": ["pawn", "figure", pawn.Pawn("white")]},
                  {"64": ["pawn", "figure", pawn.Pawn("white")]}, {"65": ["pawn", "figure", pawn.Pawn("white")]},
                  {"66": ["pawn", "figure", pawn.Pawn("white")]}, {"67": ["pawn", "figure", pawn.Pawn("white")]}],
                 [{"70": ["rook", "figure", rook.Rook("white")]}, {"71": ["knight", "figure", pawn.Pawn("white")]},
                  {"72": ["bishop", "figure", bishop.Bishop("white")]}, {"73": ["queen", "figure", pawn.Pawn("white")]},
                  {"74": ["king", "figure", pawn.Pawn("white")]}, {"75": ["bishop", "figure", bishop.Bishop("white")]},
                  {"76": ["knight", "figure", pawn.Pawn("white")]}, {"77": ["rook", "figure", rook.Rook("white")]}]]
    return board
