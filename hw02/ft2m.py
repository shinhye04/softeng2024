def ft2m(ft: float) -> float:
    return ft * 0.3048

def main():
    ft = 7
    m = ft2m(ft)

    print(f"{ft}ft -> {m:.3f}m")

if __name__ == "__main__":
    main()