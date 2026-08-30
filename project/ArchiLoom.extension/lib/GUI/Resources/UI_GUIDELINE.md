# ArchiLoom — UI Guideline & Rules (v2)

Chuẩn giao diện cho mọi WPF dialog trong `ArchiLoom.extension`.
Single source of truth về giá trị: `ArchiLoom_styles.xaml` (màu, font, style) và
`../theme.py` (hằng số cho code Python). File này là **luật dùng**.

Nguyên tắc gốc, lấy từ logo: **một nét xanh dài + đúng một nét đỏ ngắn.**
Mỗi window cũng vậy — một vệt xanh (header), một điểm đỏ (nút hành động), còn lại là trung tính.

---

## 1. Luật màu

| Gam | Được dùng ở | KHÔNG dùng cho |
|---|---|---|
| **Green** (`green_500`) | Header band, hàng đang chọn (`green_50`), dấu check, trạng thái success, ghost button an toàn | Nút Cancel/Close/Browse dạng đặc, label, chữ body |
| **Coral** (`coral_500`) | **Đúng một** nút hành động chính mỗi window, kẻ 2px dưới header, ghost button phá hủy, chữ lỗi | Label field, checkbox, tiêu đề nhóm, viền input bình thường |
| **Neutral** (`neutral_*`) | Chữ, label, viền input, kẻ bảng, nút phụ, nền — ~90% giao diện | Không giới hạn |
| **Semantic** (`info/warn/success/danger`) | Message bar + ô diff trong bảng | Nút, viền, header |

Đếm nhanh khi review một dialog: **≤ 1 vùng xanh đặc, ≤ 1 nút coral đặc.** Vượt là sai.

### Thang màu
- Green: `50 #EEF5F1` · `100 #DCEAE2` · `200 #B9D5C5` · `400 #74AF8B` · **`500 #5EA079`** · `600 #4E8A67` (hover) · `700 #3D6E52`
- Coral: `50 #FDEEEA` · `100 #FAD9D1` · `200 #F5B8A9` · `400 #EF7F68` · **`500 #EB664B`** · `600 #D8543B` (hover) · `700 #B44530`
- Neutral: `000 #FFFFFF` · `50 #F7F9F8` · `100 #EFF2F0` · `200 #E2E6E4` · `300 #CBD1CE` · `400 #A3ACA8` · `500 #78827E` · `600 #5A6360` · `700 #3F4643` · `800 #2E3230` · `900 #1E2120`
- Semantic: info `#2F6B85`/`#EDF4F8` · warn `#9A6B15`/`#FBF3E3` · success `#3D6E52`/`#EEF5F1` · danger `#B44530`/`#FDEEEA`

Không được viết hex trực tiếp trong XAML của tool. Luôn `{StaticResource ...}`.

---

## 2. Thang font — đúng 5 bậc, 2 weight

| Size | Weight | Style key | Dùng cho |
|---|---|---|---|
| 20 | SemiBold | `TitleText` | Tiêu đề trên header band |
| 14 | SemiBold | `SectionText` | Tiêu đề nhóm trong body |
| 13 | Normal / SemiBold | (mặc định TextBlock / Button) | Input, nút, body chính |
| 12 | SemiBold / Normal | `Label` / `HelpText`, `CellText` | Label field, mô tả tool, ô bảng |
| 11 | SemiBold | `OverlineText` | Overline, "STEP 2 OF 3", badge |

- Chỉ **Normal (400)** và **SemiBold (600)**. Không dùng `Bold`.
- Font UI: **Segoe UI** (có sẵn trong Revit). Dữ liệu số / Element ID / param / đường dẫn: **Consolas 12** (`MonoText`, `MonoTextBox`).
- Đoạn nhiều dòng: `LineHeight="18"` với 12px, `"20"` với 13px.
- Không đặt `FontSize` bằng số trong XAML tool — dùng `{StaticResource fs_body}` hoặc style sẵn.

---

## 3. Spacing & kích thước

Base 4px. Chỉ dùng **4 / 8 / 12 / 16 / 24**.

| Thành phần | Giá trị |
|---|---|
| Header band | 52 |
| Kẻ coral dưới header | 2, edge-to-edge, không margin |
| Gutter window | 16 (cả 4 phía) |
| TextBox / ComboBox | height 28, padding `8,0`, radius 3 |
| Button chính & phụ | height 30, min-width 92, padding `16,0`, radius 4 |
| Button ghost trong hàng/toolbar | height 26, padding `12,0` |
| Table row / column header | 28 |
| Khoảng giữa 2 field | 12 |
| Khoảng giữa 2 nhóm | 16 |
| Width window | form 460 · form + preview 620 · list/table 1040 |

Không tự đặt width khác — chọn 1 trong 3 (`WIDTH_FORM`, `WIDTH_WIZARD`, `WIDTH_LIST` trong `theme.py`).

---

## 4. Cấu trúc window bắt buộc

```
Green band 52  ─ title 20 SemiBold ─ window buttons (HeaderIconButton)
Coral rule 2px (AccentRule)              ← đúng một, edge-to-edge
Body, gutter 16
  HelpText: mô tả 1–2 dòng (cùng nội dung với tooltip trong bundle.yaml)
  [SectionText + nhóm field]…
  [Table] hoặc [Preview]
  ONE message bar (Collapsed cho tới khi có gì để nói)
Rule 1px (neutral_100)
Footer: logo wordmark góc dưới TRÁI · status (HelpText) · Cancel/Close (outline neutral) · MỘT nút coral
```

### Logo
- **Chỉ một chỗ duy nhất**: wordmark (`logo_wordmark.png`) ở **góc dưới bên trái footer**, cao 16px, **màu đầy đủ, không giảm opacity**.
- **Không** đặt logo trong header band — band xanh đã là dấu hiệu brand, thêm logo vào đó là lặp.
- Source phải set từ code (`lib/GUI/Resources/` không có pack URI từ thư mục pushbutton):
  ```python
  from GUI.theme import set_logo
  set_logo(self.footer_logo)
  ```
- `logo_mark.png` (chỉ symbol) dành cho `icon.png` của pushbutton hoặc dialog quá hẹp (< 420px).

Header **phải viết inline** trong từng file XAML (copy nguyên khối từ `_TEMPLATE_window.xaml`).
Lý do: `x:Name` và `Click="..."` bên trong `Style`/`ControlTemplate`/`DataTemplate` không được
`wpf.LoadComponent` nối vào code-behind → `AttributeError` hoặc *"Failed to create a 'Click' from the text ..."*.

---

## 5. Component & style key

**Button**
- Mặc định (không đặt `Style`) = **outline neutral** → Cancel, Close, Back, các nút phụ.
- `PrimaryButton` = coral đặc → **tối đa một** mỗi window (Run / Apply / Rename / Next). Dialog chỉ chọn chế độ (chọn xong chạy ngay) thì **không có** primary.
- `OutlineButton` = ghost xanh 26px → hành động an toàn trong hàng/toolbar (Export Excel, Rename row).
- `OutlineButtonRed` = ghost coral 26px → hành động phá hủy (Delete, Purge).
- `HeaderIconButton` = nút glyph trên header band (`✕ ─ ▢`).
- `ModeCardButton` (+ `ModeCardChip`) = ô chọn chế độ trong dialog "chọn-là-chạy".

**Dialog "chọn-là-chạy"** (2–6 lựa chọn, không có bước xác nhận — `Select2DElements`, `ModeSelect`, …)
- Width 400. `<UniformGrid Rows="2" Columns="2">`, mỗi ô là `Button Style="{StaticResource ModeCardButton}"`.
- Content: `StackPanel` → hàng trên `Border Style="{StaticResource ModeCardChip}"` chứa số `1–4` (`MonoText`) + label 13 SemiBold; hàng dưới số đếm element trong view (`MonoText`, `HelpText` màu).
- Số chip **chính là phím tắt**: `KeyDown` trên Window, `D1..D4` → handler theo `Tag`; `Escape` → `Close()`. Không vẽ icon.
- Ô không có element: `Opacity="0.5"` + text “không có trong view”. **Không** `IsEnabled="False"`, **không** ẩn — vị trí ô phải cố định để học được layout.
- Coral duy nhất trong window này là `AccentRule` dưới header.

**Input**
- `TextBox` mặc định: 28px, viền `neutral_300`, focus → viền `green_500`, `IsReadOnly` → nền `neutral_50`.
- `MonoTextBox` cho ID / số. `TextBoxInvalid` set từ code-behind khi validate fail.
- `CheckBox` / `RadioButton`: chữ `neutral_700` weight Normal (v1 là coral SemiBold — bỏ).

**Message bar** — `MessageInfo` / `MessageWarn` / `MessageSuccess` / `MessageDanger`
(+ `...Text` cho TextBlock bên trong). Chỉ **một** bar hiện cùng lúc, đặt ngay trên footer.
Từ code: `theme.set_message(self.msg_bar, self.msg_text, 'warn', "...")`.

**Table** — `ListView Style="{StaticResource Table}"`, header `TableHeaderStyle`,
ô bọc trong `RowLine`, chữ ô `CellText`, diff dùng `CellOldValue` / `CellNewValue`.
Không kẻ dọc từng ô nữa (`GridCellBorder` chỉ còn để tương thích file cũ).
Hàng chọn = `green_50`, không phải xanh đặc / xanh hệ thống.

**Rule** — `AccentRule` (coral 2px dưới header) và `Rule` (hairline neutral). `Divider` là legacy.

---

## 6. Checklist khi làm tool mới

1. Copy `_TEMPLATE_window.xaml` + `_TEMPLATE_script.py`, đổi tên.
2. `apply_theme(self)` **trước** `forms.WPFWindow.__init__`.
3. Header copy inline, đổi `main_title` từ `__title__`.
4. Chỉ 1 nút `PrimaryButton` (dialog chọn chế độ: không có); mọi nút khác để mặc định hoặc ghost.
5. Không hex, không `FontSize` số, không `Margin` ngoài 4/8/12/16/24 trong XAML.
6. Width chọn 460 / 620 / 1040 (dialog chọn chế độ: 400).
7. Footer có `<Image x:Name="footer_logo"/>` góc trái + `set_logo(self.footer_logo)` trong `__init__`.
8. `__doc__` trong `script.py` và `tooltip:` trong `bundle.yaml` giống nhau từng chữ.
9. Đọc lại cú pháp IronPython 2.7 (không f-string, không type hint) — không có test runner.
10. Nói rõ với user: **chưa test trong Revit**, cần Reload pyRevit và bấm nút thật.

---

## 7. Đổi gì so với v1

| v1 | v2 | Vì sao |
|---|---|---|
| `text_label` = `#EB664B` (label đỏ) | `#5A6360` neutral | Đỏ mất hết trọng số khi nằm ở mọi label |
| CheckBox coral SemiBold | neutral 700 Normal | Cùng lý do |
| Button mặc định = xanh đặc | outline neutral | Cancel/Browse không được cạnh tranh với nút chính |
| Header 56, title 18 Bold | 52, 20 SemiBold | Bold 18 nhìn nặng trong Revit; thang font còn 5 bậc |
| `Divider` coral thụt lề 16 | `AccentRule` 2px edge-to-edge + `Rule` hairline | Vệt đỏ trở thành nét ký tên, không phải đường phân cách chung |
| `GridCellBorder` kẻ dọc từng ô | `RowLine` chỉ kẻ ngang | Bảng nhiều cột đọc rối |
| Input 26 | 28 | Khớp row height và ComboBox |
| Chỉ 2 gam brand | + thang neutral 11 bậc + 4 semantic | Có chỗ để phân cấp mà không cần dùng brand |
| Không có logo trong dialog | Wordmark góc dưới trái footer | Ký tên đúng một lần, không đè lên tiêu đề |

Mọi key của v1 vẫn tồn tại (alias) → các dialog hiện có load được và tự đổi theo, không cần sửa file.
Việc cần sửa tay từng file: xem `APPLY_UI_STANDARD.md` ở root extension.
