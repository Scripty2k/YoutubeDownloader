def convert_to_format(input_file: str, output_format: str):
    from pydub import AudioSegment
    import os

    # Determine the output file name
    base = os.path.splitext(input_file)[0]
    output_file = f"{base}.{output_format}"

    # Convert to the desired format
    if output_format == "mp3":
        audio = AudioSegment.from_file(input_file)
        audio.export(output_file, format="mp3")
    elif output_format == "wav":
        audio = AudioSegment.from_file(input_file)
        audio.export(output_file, format="wav")
    else:
        raise ValueError("Unsupported output format. Please choose 'mp3' or 'wav'.")

    return output_file