INPUT = "nhoJ (Griffith) nodnoL saw (an) (American) ,tsilevon ,tsilanruoj (and) laicos .tsivitca ((A) reenoip (of) laicremmoc noitcif (and) naciremA ,senizagam (he) saw eno (of) (the) tsrif (American) srohtua (to) emoceb (an) lanoitanretni ytirbelec (and) nrae a egral enutrof (from) ).gnitirw"

CORRECT_ANSWER = "John Griffith London was an American novelist, journalist, and social activist. (A pioneer of commercial fiction and American magazines, he was one of the first American authors to become an international celebrity and earn a large fortune from writing.)"


def fix_text(mystr):
  #Split the text into a list of words.
    words = mystr.split()
    corrected_words = []
    for word in words:
        if word.startswith("(") and word.endswith(")"):
            # Add the words inside the parentheses without the parentheses
            corrected_words.append(word[1:-1])
        else:
            # Reverse the other words and add them
            corrected_words.append(word[::-1])
    # Return the merged text after going through the correction process.
    return ' '.join(corrected_words)

if __name__ == "__main__":
    # Text correction process
    corrected_text = fix_text(INPUT)
    print("Corrected text:", corrected_text)

    # Check the result
    print("Correct!" if corrected_text == CORRECT_ANSWER else "Sorry, it does not match with the correct answer.")