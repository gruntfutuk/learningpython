#!/usr/bin/env python3
#
# function to return longer alphabatical sequence in supplied string
# Note: ignore class
#       if more than one sequence of same length, return first of that length


def alphaseq(source):
  if len(source) <= 1: # check for empty or one character source string
    return source
  candidate = source[0]  # longest sequence found so far that we would return
  newcand = source[0]    # build next sequence from source until sequence breaks
  for ch in source[1:]:  # continue search from 2nd char
    if ch.lower() >= newcand[-1].lower(): # check sequence not broken, ignore case
      newcand += ch  # sequence continues, so append char to new candidate
    else:
      newcand = ch  # otherwise we are start a new sequence
    if len(newcand) > len(candidate):  # if new sequence longer than candidate
      candidate = newcand              # then make it the candidate for return
  return candidate

 
def main():
  while True:
    review = input("\nEnter word/phrase (enter alone to exit):")
    if not review:
      break
    longest  = alphaseq(review)
    print(f'\nLongest sequence: \'{longest}\' at {len(longest)} char(s) long.\n\n')

main()  # execute on repl.it; in py file: if __name__ == "__main__": main()