import sys

md5_hash, sha1_hash = sys.argv[1], sys.argv[2]

# ! \begin{table}[h!]
print(r"\begin{table}[h!]")
# !   {
print(r"{")
# !     \ttfamily\tiny
print(r"\ttfamily\tiny")
# !     \begin{flushright}
print(r"\begin{flushright}")
# !       MD5:[md5_hash]
print(f"MD5:{md5_hash}")
# !     \end{flushright}
print(r"\end{flushright}")
# !     \vspace{-5ex}
print(r"\vspace{-5ex}")
# !   }
print(r"}")
# !   \ttfamily\footnotesize
print(r"\ttfamily\footnotesize")
# !   \setlength{\tabcolsep}{0.1cm}
print(r"\setlength{\tabcolsep}{0.1cm}")
# !   \newcolumntype{k}{p{1cm}}
print(r"\newcolumntype{k}{p{1cm}}")
# !   \newcolumntype{v}{c}
print(r"\newcolumntype{v}{c}")
# !   \begin{tabular}{|k|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|}
print(r"\begin{tabular}{|k|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|v|}")
# !     \hline
print(r"\hline")
md5_row, md5_rowpad = " & ".join(md5_hash), " & ".join("-" * 8)
print(f"MD5 & {md5_row} & {md5_rowpad} \\tabularnewline \\hline")
sha1_row = " & ".join(sha1_hash)
print(f"SHA1 & {sha1_row} \\tabularnewline \\hline")
# !   \end{tabular}
print(r"\end{tabular}")
# !   {
print(r"{")
# !     \ttfamily\tiny
print(r"\ttfamily\tiny")
# !     \vspace{-5ex}
print(r"\vspace{-5ex}")
# !     \begin{flushright}
print(r"\begin{flushright}")
# !       SHA1:[sha1_hash]
print(f"SHA1:{sha1_hash}")
# !     \end{flushright}
print(r"\end{flushright}")
# !   }
print(r"}")
# !   \end{table}
print(r"\end{table}")
