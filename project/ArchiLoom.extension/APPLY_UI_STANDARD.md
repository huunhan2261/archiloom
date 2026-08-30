# Áp UI Standard v2 vào extension

Hướng dẫn đưa toàn bộ brand guideline + rule vào `ArchiLoom.extension` và cập nhật những gì đang có.

---

## Bước 1 — Copy 6 file (ghi đè)

Từ thư mục project này, copy đúng theo cấu trúc, ghi đè file cũ:

| File | Trạng thái |
|---|---|
| `lib/GUI/Resources/ArchiLoom_styles.xaml` | **ghi đè** — palette + type scale + toàn bộ style |
| `lib/GUI/theme.py` | **ghi đè** — hằng số màu/size + `set_message()` |
| `lib/GUI/Resources/_TEMPLATE_window.xaml` | **ghi đè** — template window v2 |
| `lib/GUI/Resources/_TEMPLATE_script.py` | **ghi đè** — thêm `set_message` vào pattern |
| `lib/GUI/Resources/UI_GUIDELINE.md` | mới — **luật dùng**, đọc cái này khi làm tool |
| `lib/GUI/Resources/logo_mark.png` · `logo_wordmark.png` | mới — `logo_mark` cho icon, `logo_wordmark` cho footer |

> Backup `ArchiLoom_styles.xaml` cũ trước khi ghi đè (đổi tên thành `ArchiLoom_styles.v1.bak`), để rollback nếu Revit báo lỗi resource.

Xong bước 1 → pyRevit **Reload** → mở thử 2–3 dialog. **Không cần sửa file XAML nào**, mọi dialog hiện có đã tự đổi:
label đỏ → neutral, checkbox đỏ → neutral, nút phụ xanh đặc → outline neutral, input 26 → 28,
kẻ bảng bỏ kẻ dọc, hàng chọn xanh nhạt. Mọi key của v1 vẫn còn (alias) nên không có `StaticResource` nào bị vỡ.

---

## Bước 2 — Sửa tay phần header (2 dòng mỗi file)

Chỉ phần geometry của header là inline trong từng XAML nên không tự đổi được. Find & replace giống nhau ở mọi file:

**2.1 — chiều cao band**
```
find:     Background="{StaticResource brand_green}" Height="56"
replace:  Background="{StaticResource green_500}" Height="52"
```

**2.2 — tiêu đề**
```
find:     FontSize="18" FontWeight="Bold"
                       VerticalAlignment="Center"
                       Foreground="{StaticResource text_on_brand}"
replace:  Style="{StaticResource TitleText}"
```
(nếu format khác chút: chỉ cần bỏ `FontSize`/`FontWeight`/`Foreground`/`VerticalAlignment` trên `main_title` và đặt `Style="{StaticResource TitleText}"`)

**2.3 — nút window trên header**
Thêm `Style="{StaticResource HeaderIconButton}"` vào các Button `X` / `_` / `▢`, và bỏ
`Width="28" Height="28" FontSize="12" Background="Transparent" Foreground="{StaticResource text_on_brand}"`.

**2.4 — vệt coral**
Sau `</Grid>` của header, thay `<Border Style="{StaticResource Divider}"/>` (đang thụt lề 16) bằng:
```xml
<Border Style="{StaticResource AccentRule}"/>
```
rồi cho phần mô tả `Margin="16,16,16,0"` và `Style="{StaticResource HelpText}"`.

### 23 file XAML cần bước 2

Detailing.panel — `ApplySheetLayout_window`, `DetailItemLayout`, `DetailItemViews`, `DetailTypeList`, `ImportReview`, `SheetPicker`, `ManageLineStyles_window`, `QuickLineStyle_window`, `SaveSheetLayout_window`, `Select2DElements_window`, `SyncDetailItemParams_window`
Family.panel — `BatchFamilyRename`, `BatchFamilyTypeRename`, `CategoryFilter`, `ModeSelect`, `DetailItemFromSelection`, `FamilyDuplicate`, `FamilyRename`, `PurgeFamilyParameters`
Sandbox.panel — `RelayoutSettings_window`, `ResizeFilledRegion_window`, `TagDetailItems`
lib/GUI — `SelectFromDict`

Làm dần cũng được: file chưa sửa vẫn chạy, chỉ là header còn 56/18 Bold.

---

## Bước 3 — Nâng cấp tùy chọn (làm khi rảnh, từng file)

- **Table**: đổi `<ListView ...>` sang `Style="{StaticResource Table}"`, cell wrap bằng `RowLine` thay `GridCellBorder`, chữ ô `CellText`, diff `CellOldValue`/`CellNewValue`, header cột `TableHeaderStyle`.
- **Message bar**: thay các `forms.alert()` cho thông báo nhẹ bằng một `Border x:Name="msg_bar"` + `set_message(...)`.
- **Width**: đưa về 460 / 620 / 1040.
- **Logo footer** (chuẩn mới — xem mockup 1a/1b/1c): thêm vào footer Grid một cột `Width="Auto"` ở ngoài cùng bên trái:
```xml
<Image x:Name="footer_logo" Grid.Column="0" Height="16"
       Margin="0,0,16,0" VerticalAlignment="Center"
       HorizontalAlignment="Left" Stretch="Uniform"/>
```
rồi trong `__init__`, sau `forms.WPFWindow.__init__`:
```python
from GUI.theme import set_logo
set_logo(self.footer_logo)
```
`lib/GUI/Resources/` không có pack URI từ thư mục pushbutton nên bắt buộc set Source từ code — `set_logo()` đã làm sẵn (absolute path + đúng chiều cao 16px).
Wordmark **để màu đầy đủ, không giảm opacity**, và **không đặt logo trong header band**.

---

## Bước 4 — Cập nhật CLAUDE.md

Thay **toàn bộ** mục `## GUI style (bắt buộc cho tool mới có dialog)` bằng đoạn dưới:

```markdown
## GUI style (bắt buộc cho tool mới có dialog)
Mọi WPF dialog theo **ArchiLoom UI Standard v2**. Luật đầy đủ: `lib/GUI/Resources/UI_GUIDELINE.md` — đọc trước khi viết XAML.

Tóm tắt bắt buộc:
- **Màu**: green `#5EA079` chỉ cho header band / hàng chọn / dấu check / success. Coral `#EB664B` chỉ cho **đúng một** nút hành động chính mỗi window + kẻ 2px dưới header. Còn lại dùng thang `neutral_*`. Semantic (`info/warn/success/danger`) chỉ trong message bar và ô diff. **Không viết hex trong XAML của tool** — luôn `{StaticResource ...}`.
- **Font**: đúng 5 size (20 `TitleText` / 14 `SectionText` / 13 body & button / 12 `Label`,`HelpText`,`CellText` / 11 `OverlineText`), đúng 2 weight (Normal, SemiBold — **không Bold**). Segoe UI cho UI, Consolas 12 (`MonoText`) cho ID/số/param/path. Không đặt `FontSize` bằng số.
- **Spacing**: chỉ 4/8/12/16/24. Gutter window 16. Header 52, kẻ coral 2, input 28, button 30 (ghost 26), row 28. Width window chọn 460 / 620 / 1040.
- **Button**: mặc định = outline neutral (Cancel/Close/Browse). `PrimaryButton` = coral, **một cái** mỗi window. `OutlineButton` (xanh) / `OutlineButtonRed` (phá hủy) = ghost 26px trong hàng/toolbar. `HeaderIconButton` cho nút trên header.
- **Logo**: wordmark `logo_wordmark.png` ở **góc dưới bên trái footer**, cao 16px, màu đầy đủ (không giảm opacity). Không đặt logo trong header band. Source set từ code: `set_logo(self.footer_logo)` — `lib/GUI/Resources/` không có pack URI từ thư mục pushbutton.
- **Áp dụng**: `from GUI.theme import apply_theme, set_logo, set_message`; `apply_theme(self)` gọi **TRƯỚC** `forms.WPFWindow.__init__(self, xaml)` (`wpf.LoadComponent` resolve `{StaticResource}` ngay lập tức; gọi sau sẽ lỗi "Cannot find resource named ...").
- **Header (band xanh + title + nút X) phải viết inline trong từng file XAML** — copy nguyên khối `<Grid>` từ `_TEMPLATE_window.xaml`, KHÔNG bọc trong `Style`/`ContentTemplate`/`DataTemplate`: `x:Name` và `Click="..."` bên trong template không được `wpf.LoadComponent` nối vào code-behind (template chỉ áp lúc `ShowDialog()`, quá trễ) → `AttributeError` hoặc `Failed to create a 'Click' from the text ...`. Cùng lý do đó, event handler trong `DataTemplate`/`CellTemplate` cũng không chạy — dùng `{Binding}` và `DataTrigger`.
- **Table**: `ListView Style="{StaticResource Table}"`, header `TableHeaderStyle`, ô bọc `RowLine` (chỉ kẻ ngang — `GridCellBorder` là legacy), chữ ô `CellText`, diff `CellOldValue`/`CellNewValue`, hàng chọn `green_50`.
- **Thông báo**: một `Border x:Name="msg_bar"` + `TextBlock x:Name="msg_text"` ngay trên footer, đổ nội dung bằng `set_message(self.msg_bar, self.msg_text, 'warn', "...")`. Không hiện 2 bar cùng lúc.
- **Tạo tool mới**: copy `lib/GUI/Resources/_TEMPLATE_window.xaml` + `_TEMPLATE_script.py`, đổi tên. Hai file này đã đúng thứ tự/pattern — theo sát, đừng tự sắp xếp lại.
```

Ví dụ tham chiếu trong CLAUDE.md (mục `lib/`): đổi "`Family Rename.pushbutton/` theo đúng brand hiện tại" →
**"`Family Rename.pushbutton/` (sau khi làm bước 2) hoặc `_TEMPLATE_window.xaml` là ví dụ chuẩn v2."**

---

## Rủi ro cần test trong Revit

Chưa test — bắt buộc Reload pyRevit và bấm nút thật. Ba điểm dễ vỡ nhất, theo thứ tự:

1. `TableRowStretch` giờ có `ControlTemplate` với `GridViewRowPresenter` (để hàng chọn xanh nhạt thay vì xanh hệ thống). Nếu bảng nào render trống hoặc lỗi `Columns`, xóa khối `<Setter Property="Template">` trong style đó — mất màu hàng chọn, còn lại vẫn đúng.
2. `<sys:Double x:Key="fs_*">` cần `xmlns:sys="clr-namespace:System;assembly=mscorlib"` (đã có trong file). Nếu IronPython báo lỗi namespace, thay `{StaticResource fs_body}` bằng số trong chính file styles (chỉ trong file đó).
3. `Typography.Capitals` trên `OverlineText` — nếu không có hiệu lực thì viết chữ HOA sẵn trong `Text=`.

Rollback: đổi `ArchiLoom_styles.v1.bak` về tên cũ là xong (các file XAML tool chưa bị sửa gì ở bước 1).
