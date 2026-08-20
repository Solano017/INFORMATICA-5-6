import qrcode
def main():
    song = "https://youtu.be/aDCcLQto5BM?si=Hn3GwkBZhX_a1Rgb"
    qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
    qr.add_data("song")
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("my-qrcode.png")


if __name__ == "__main__":
    main()
