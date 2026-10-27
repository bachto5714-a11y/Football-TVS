# ==========================================
# FOOTBALL TRANSFER VALUE SCORE (TVS) SYSTEM
# Ultimate Production-Ready Version (with Superstar Multiplier)
# ==========================================

# ==========================================
# HƯỚNG DẪN THỨ TỰ NHẬP INPUT (INPUT ORDER)
# ==========================================
# 1. Tên cầu thủ (Ten)
# 2. Vị trí (Pois) -> (ST, CF, LW, RW, RS, LS, RF, LF, CM, CDM, CAM, LM, RM, CB, LB, RB, RWB, LWB, GK, SW)
# 3. Thông số riêng theo vị trí:
#    - Nếu là DEF (CB, LB, RB, RWB, LWB): Nhập 2 số (Tackle, Block) cách nhau bằng dấu cách.
#    - Nếu là GK, SW: Nhập 2 số (Goal_conceded, Pressingout_pass) cách nhau bằng dấu cách.
#    - Nếu là ATT, MID: Bỏ qua bước này, nhập ở bước sau.
# 4. OVR (0 đến 99)
# 5. Tuổi (Age)
# 6. Nếu là ATT, MID: Nhập 2 số (Goal, assist) cách nhau bằng dấu cách.
# 7. Giá trị cầu thủ / Giá mua (Value - triệu Euro)
# 8. Ngân sách hiện có (Budget - triệu Euro)
# 9. Tên giải đấu (League) -> (PremierLeague, Laliga, Bundesliga, SerieA, Ligue1)
# 10. Tên Câu lạc bộ (Club) -> Phải khớp chính xác với từ điển CLB
# ==========================================

# =========================
# 1. POSITION DATA
# =========================
DEF_POS = {"CB", "LB", "RB", "RWB", "LWB"}
ATT = {"ST", "CF", "LW", "RW", "RS", "LS", "RF", "LF"}
MID = {"CM", "CDM", "CAM", "LM", "RM"}
GK = {"GK", "SW"}

# =========================
# 2. CLUB CLASSIFICATION
# =========================
CLUBS = {
    "PremierLeague": {
        "Strong": ["Manchester City", "Liverpool", "Arsenal"],
        "Mid": ["Manchester United", "Tottenham", "Chelsea", "West Ham"],
        "Weak": [
            "Aston Villa", "Bournemouth", "Brentford", "Brighton", "Burnley",
            "Crystal Palace", "Everton", "Fulham", "Leeds United", 
            "Newcastle United", "Nottingham Forest", "Sunderland", "Wolverhampton"
        ]
    },
    "Laliga": {
        "Strong": ["Real Madrid", "Barcelona", "Atletico Madrid"],
        "Mid": ["Real Sociedad", "Real Betis", "Athletic Bilbao"],
        "Weak": [
            "Celta Vigo", "Deportivo Alaves", "Elche", "Espanyol", "Getafe",
            "Levante", "Malaga", "Osasuna", "Racing", "Rayo Vallecano",
            "RC Deportivo", "Sevilla", "Valencia", "Villarreal"
        ]
    },
    "Bundesliga": {
        "Strong": ["Bayern Munich", "Borussia Dortmund"],
        "Mid": ["RB Leipzig", "Bayer Leverkusen", "Union Berlin"],
        "Weak": [
            "Werder Bremen", "Hoffenheim", "Augsburg", "Mainz", "Stuttgart",
            "Eintracht Frankfurt", "FC Koln", "Borussia Monchengladbach", 
            "Freiburg", "Schalke 04", "Hamburger SV", "Paderborn", "Elversberg"
        ]
    },
    "SerieA": {
        "Strong": ["Inter", "AC Milan", "Juventus"],
        "Mid": ["Napoli", "Roma", "Lazio", "Atalanta"],
        "Weak": [
            "Bologna", "Cagliari", "Como", "Fiorentina", "Frosinone",
            "Genoa", "Lecce", "Monza", "Parma", "Sassuolo", "Torino", "Udinese", "Venezia"
        ]
    },
    "Ligue1": {
        "Strong": ["Paris Saint-Germain"],
        "Mid": ["Monaco", "Marseille", "Lyon", "Lille"],
        "Weak": [
            "Lens", "Rennes", "Strasbourg", "Toulouse", "Lorient",
            "Paris FC", "Brest", "Angers", "Le Havre", "Auxerre", "Nice", "Troyes", "Le Mans"
        ]
    }
}

# =========================
# 3. CLUB COEFFICIENTS
# =========================
COEFFICIENTS = {
    "PremierLeague": {"Strong": 1.20, "Mid": 1.10, "Weak": 1.00},
    "Laliga": {"Strong": 1.15, "Mid": 1.00, "Weak": 0.90},
    "Bundesliga": {"Strong": 1.15, "Mid": 1.05, "Weak": 0.90},
    "SerieA": {"Strong": 1.15, "Mid": 1.05, "Weak": 0.90},
    "Ligue1": {"Strong": 1.15, "Mid": 1.00, "Weak": 0.90}
}

# =========================
# 4. INPUT SECTION & VALIDATION
# =========================
Ten = input().strip()
Pois = input().strip().upper()

if Pois not in DEF_POS | ATT | MID | GK:
    raise ValueError("Invalid position specified.")

# Lấy thông số đặc thù theo vị trí
if Pois in DEF_POS:
    Tackle, Block = map(int, input().split())
elif Pois in GK:
    Goal_conceded, Pressingout_pass = map(int, input().split())

OVR = int(input())
if not 0 <= OVR < 100:
    raise ValueError("OVR must be between 0 and 99.")

Age = int(input())
if Age <= 0:
    raise ValueError("Age must be a positive integer.")

if Pois in ATT | MID:
    Goal, assist = map(int, input().split())

Value = int(input())
if Value <= 0:
    raise ValueError("Player Value must be greater than 0.")

Budget = int(input())
if Budget < 0:
    raise ValueError("Budget cannot be negative.")

# Chuẩn hóa tên giải đấu (bỏ khoảng trắng để khớp từ điển an toàn)
League = input().strip().replace(" ", "")
Club = input().strip()

# =========================
# 5. CLUB LOOKUP & BUDGET CHECK
# =========================
if League not in CLUBS:
    raise ValueError(f"Unknown league '{League}'. Make sure it matches format (e.g., PremierLeague).")

team_tier = None
for tier, teams in CLUBS[League].items():
    if Club in teams:
        team_tier = tier
        break

if team_tier is None:
    raise ValueError(f"Club '{Club}' not found in league '{League}'.")

team_coefficient = COEFFICIENTS[League][team_tier]

# Kiểm tra ngân sách
if Budget < Value:
    print(f"\n--- TRANSFER REPORT ---")
    print(f"Player: {Ten}")
    print(f"Club: {Club}")
    print(f"Price: €{Value}M")
    print(f"Your budget: €{Budget}M")
    print("Transfer Status: NOT ENOUGH MONEY")
    raise SystemExit

remaining_budget = Budget - Value

# =========================
# 6. MODEL COEFFICIENTS (OVR Bonus, Age Factor & Superstar Multiplier)
# =========================

# A. OVR Bonus liên tục (Không nhảy khúc biên)
ovr_bonus = max(0.0, min(5.0, 5.0 - (OVR - 75) * 0.25))

# B. Hệ số độ tuổi (Age Growth & Depreciation Curve)
if Age <= 21:
    age_coefficient = 1.15  # Sao trẻ: Tiềm năng phát triển lớn
elif 22 <= Age <= 29:
    age_coefficient = 1.00  # Độ tuổi chín muồi (Prime)
elif 30 <= Age <= 34:
    age_coefficient = 0.90  # Bắt đầu lớn tuổi, khấu hao nhẹ
else:
    age_coefficient = 0.80  # Lão tướng: Giá trị dài hạn thấp

# C. Hệ số ngôi sao (Superstar Multiplier - Bù đắp mẫu số Value quá lớn của các siêu sao)
if OVR >= 90:
    superstar_multiplier = 1.40  # Siêu sao toàn cầu (World-class tier)
elif 85 <= OVR < 90:
    superstar_multiplier = 1.15  # Cầu thủ hàng đầu (Top player tier)
else:
    superstar_multiplier = 1.00  # Tiêu chuẩn thông thường

# =========================
# 7. CALCULATING TVS
# =========================
if Pois in ATT | MID:
    tvs = OVR * (Goal + assist + ovr_bonus) / Value
elif Pois in DEF_POS:
    tvs = OVR * (Tackle + Block + ovr_bonus) / Value
else:
    # Tránh hiệu suất thủ môn bị âm hoặc bằng 0
    gk_performance = Pressingout_pass - Goal_conceded + ovr_bonus
    if gk_performance <= 0:
        gk_performance = 1 
    tvs = OVR * gk_performance / Value

# Áp dụng toàn bộ hệ số: CLB, Độ tuổi và Ngôi sao
tvs *= team_coefficient * age_coefficient * superstar_multiplier

# =========================
# 8. RECOMMENDATION & REASON (Có vùng đệm Borderline)
# =========================
if tvs >= 42:
    recommendation = "RẤT ĐÁNG MUA (Highly Recommended)"
    reason = "Hiệu năng (TVS) vượt trội, mức đầu tư mang lại giá trị sử dụng cực kỳ cao."
elif 38 <= tvs < 42:
    recommendation = "CÂN NHẮC KỸ - TIỆM CẬN NGƯỠNG (Borderline / Consider+)"
    reason = "TVS nằm sát ngưỡng cao, cần trinh sát thêm phong độ thực tế trước khi chốt."
elif 20 <= tvs < 38:
    recommendation = "CÂN NHẮC MUA (Consider)"
    reason = "Hiệu năng ở mức ổn định, phù hợp với mức giá chuyển nhượng tầm trung."
else:
    recommendation = "KHÔNG NÊN MUA (Not Recommended)"
    reason = "TVS thấp, giá trị chuyển nhượng quá đắt đỏ so với đóng góp thực tế."

# =========================
# 9. OUTPUT REPORT
# =========================
print(f"\n========================================")
print(f"          TRANSFER REPORT               ")
print(f"========================================")
print(f"Player Name      : {Ten} (Age: {Age})")
print(f"Club & Tier      : {Club} [{team_tier}]")
print(f"League           : {League}")
print(f"Club Coefficient : {team_coefficient}")
print(f"Age Coefficient  : {age_coefficient}")
print(f"Superstar Multi. : {superstar_multiplier}")
print(f"Price / Budget   : €{Value}M / €{Budget}M (Rem: €{remaining_budget}M)")
print(f"----------------------------------------")
print(f"Final TVS Score  : {tvs:.2f}")
print(f"Recommendation   : {recommendation}")
print(f"Reason           : {reason}")
print(f"========================================")