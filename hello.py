age = 25
has_licence = True
drunk = True

can_drive = age >= 16 and has_licence and not drunk
print = f"That man {can_drive}"