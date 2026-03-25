from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Cau hinh hien thi chung cho bieu do
sns.set_theme(style="whitegrid", palette="deep")
plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["axes.titlesize"] = 14
plt.rcParams["axes.labelsize"] = 11


DATA_FILE = Path(__file__).with_name("pseudo_facebook.csv")
OUTPUT_DIR = Path(__file__).with_name("figures")


def print_section(title: str) -> None:
    """Phan tich."""
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def save_and_show(filename: str) -> None:
    """Luu bieu do vao thu muc figures va hien thi len man hinh."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / filename, dpi=300, bbox_inches="tight")
    plt.show()


def load_data() -> pd.DataFrame:
    """tien xu ly du lieu."""
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Khong tim thay tep du lieu: {DATA_FILE}")

    df = pd.read_csv(DATA_FILE)
    df = df.dropna(subset=["gender"]).copy()

    return df


def basic_overview(df: pd.DataFrame) -> None:
    """tong quan ve bo du lieu."""
    print_section("1. Tong quan bo du lieu")
    print(f"So dong: {df.shape[0]}")
    print(f"So cot: {df.shape[1]}")
    print("\nCac cot trong du lieu:")
    print(df.columns.tolist())

    print("\n5 dong dau tien:")
    print(df.head())

    print("\nKieu du lieu cua tung cot:")
    print(df.dtypes)

    print("\nSo gia tri thieu o moi cot:")
    print(df.isnull().sum())


def descriptive_statistics(df: pd.DataFrame) -> None:
    """thong ke mo ta cho cac bien so."""
    print_section("2. Thong ke mo ta")
    numeric_cols = [
        "age",
        "dob_day",
        "dob_month",
        "tenure",
        "friend_count",
        "friendships_initiated",
        "likes",
        "likes_received",
        "mobile_likes",
        "mobile_likes_received",
        "www_likes",
        "www_likes_received",
    ]
    print(df[numeric_cols].describe().round(2))


def plot_age_distribution(df: pd.DataFrame) -> None:
    """Phan tich phan bo do tuoi cua nguoi dung."""
    print_section("3. Phan tich do tuoi")
    print("Tuoi nho nhat:", df["age"].min())
    print("Tuoi lon nhat:", df["age"].max())
    print("Tuoi trung binh:", round(df["age"].mean(), 2))
    print("Tuoi trung vi:", round(df["age"].median(), 2))

    plt.figure()
    sns.histplot(df["age"], bins=30, kde=True, color="#1f77b4")
    plt.title("Phan bo do tuoi cua nguoi dung Facebook")
    plt.xlabel("Tuoi")
    plt.ylabel("So nguoi dung")
    save_and_show("01_phan_bo_do_tuoi.png")


def plot_birth_day_distribution(df: pd.DataFrame) -> None:
    """Phan tich ngay sinh trong thang."""
    print_section("4. Phan tich ngay sinh (dob_day)")
    day_counts = df["dob_day"].value_counts().sort_index()
    print("So nguoi dung theo ngay sinh:")
    print(day_counts)

    plt.figure()
    sns.countplot(data=df, x="dob_day", order=range(1, 32), color="#2ca02c")
    plt.title("Phan bo nguoi dung theo ngay sinh trong thang")
    plt.xlabel("Ngay sinh")
    plt.ylabel("So nguoi dung")
    save_and_show("02_phan_bo_ngay_sinh.png")


def plot_birth_month_distribution(df: pd.DataFrame) -> None:
    """Phan tich thang sinh."""
    print_section("5. Phan tich thang sinh (dob_month)")
    month_counts = df["dob_month"].value_counts().sort_index()
    print("So nguoi dung theo thang sinh:")
    print(month_counts)

    plt.figure()
    sns.countplot(data=df, x="dob_month", order=range(1, 13), color="#ff7f0e")
    plt.title("Phan bo nguoi dung theo thang sinh")
    plt.xlabel("Thang sinh")
    plt.ylabel("So nguoi dung")
    save_and_show("03_phan_bo_thang_sinh.png")


def plot_gender_analysis(df: pd.DataFrame) -> None:
    """So sanh quy mo va muc do tuong tac theo gioi tinh."""
    print_section("6. Phan tich gioi tinh")
    print("So luong nguoi dung theo gioi tinh:")
    print(df["gender"].value_counts())

    print("\nLikes trung binh theo gioi tinh:")
    print(df.groupby("gender", observed=False)["likes"].mean().round(2))

    plt.figure()
    sns.countplot(data=df, x="gender", color="#4c72b0")
    plt.title("Phan bo gioi tinh")
    plt.xlabel("Gioi tinh")
    plt.ylabel("So nguoi dung")
    save_and_show("04_phan_bo_gioi_tinh.png")

    plt.figure()
    sns.barplot(data=df, x="gender", y="likes", estimator="mean", errorbar=None, color="#dd8452")
    plt.title("So sanh likes trung binh theo gioi tinh")
    plt.xlabel("Gioi tinh")
    plt.ylabel("Likes trung binh")
    save_and_show("05_likes_theo_gioi_tinh.png")


def plot_age_group_and_likes(df: pd.DataFrame) -> None:
    """So sanh likes giua cac nhom tuoi."""
    print_section("7. Moi lien he giua nhom tuoi va likes")

    age_group = pd.cut(df["age"], bins=8)
    age_likes = df.groupby(age_group, observed=False)["likes"].mean()
    print("Likes trung binh theo nhom tuoi:")
    print(age_likes.round(2))

    plt.figure()
    age_likes.plot(kind="bar", color="#d62728")
    plt.title("Likes trung binh theo nhom tuoi")
    plt.xlabel("Nhom tuoi")
    plt.ylabel("Likes trung binh")
    save_and_show("06_likes_theo_nhom_tuoi.png")


def plot_tenure_by_friend_count(df: pd.DataFrame) -> None:
    """Phan tich thoi gian su dung trung binh theo nhom so ban be."""
    print_section("8. Thoi gian su dung trung binh theo nhom so ban be")

    friend_group = pd.cut(df["friend_count"], bins=8)
    tenure_by_friend_count = df.groupby(friend_group, observed=False)["tenure"].mean()
    print("Thoi gian su dung trung binh theo nhom so ban be:")
    print(tenure_by_friend_count.round(2))

    plt.figure()
    tenure_by_friend_count.plot(kind="bar", color="#8c564b")
    plt.title("Thoi gian su dung trung binh theo nhom so ban be")
    plt.xlabel("Nhom friend_count")
    plt.ylabel("Tenure trung binh (ngay)")
    save_and_show("07_tenure_theo_nhom_ban_be.png")


def plot_correlation_heatmap(df: pd.DataFrame) -> None:
    """Ve ma tran tuong quan giua cac bien so."""
    print_section("9. Ma tran tuong quan")

    numeric_df = df.select_dtypes(include="number")
    correlation_matrix = numeric_df.corr()
    print(correlation_matrix.round(2))

    plt.figure(figsize=(12, 9))
    sns.heatmap(
        correlation_matrix,
        cmap="coolwarm",
        annot=True,
        fmt=".2f",
        linewidths=0.5,
        linecolor="white",
    )
    plt.title("Ma tran tuong quan giua cac bien so")
    save_and_show("08_ma_tran_tuong_quan.png")
    
def main() -> None:
    df = load_data()
    basic_overview(df)
    descriptive_statistics(df)
    plot_age_distribution(df)
    plot_birth_day_distribution(df)
    plot_birth_month_distribution(df)
    plot_gender_analysis(df)
    plot_age_group_and_likes(df)
    plot_tenure_by_friend_count(df)
    plot_correlation_heatmap(df)
    print_final_conclusion(df)
    
if __name__ == "__main__":
    main()
