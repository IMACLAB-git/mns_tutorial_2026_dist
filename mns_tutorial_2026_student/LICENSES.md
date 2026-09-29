# 라이선스

## 이 실습 자료

| 대상 | 라이선스 |
|---|---|
| 문서와 화면 캡처: `README.md`, `GUIDE.md`, `guide_img/`, `reference/`와 `example_run/`의 문서 | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — © 2026 SLEE |
| 코드: `reference/papers/collect.py`, `reset.ps1` | MIT License (아래 전문) — © 2026 SLEE |

다시 쓸 때는 출처("MNS 2026 실습: 논문에서 RQ까지, SLEE")를 밝힌다.

**예외: 논문에서 온 것은 원 라이선스를 따른다.**
- `backup_pdf/`의 PDF, `example_run/explainer/figures/`의 그림: 아래 표
- 논문 그림이 보이는 화면 캡처: `guide_img/06e_figures.png`(Johnson 2023 Fig. 1b–e, CC BY 4.0), `06f_claim1.png`(Zhang 2023 Fig. 2a, CC BY 4.0 / Park 2025 Fig. 1, CC BY-NC-ND 4.0), `06g_claim1_new.png`(Park 2025 Fig. 1 일부가 화면에 걸림, CC BY-NC-ND 4.0)
- 위키 페이지와 설명 페이지에 옮긴 논문의 문장·수치는 각 논문에서 인용한 것이다. 출처는 해당 페이지에 적혀 있다.

<details>
<summary>MIT License 전문</summary>

```
MIT License

Copyright (c) 2026 SLEE

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

</details>

---

# 논문 자료의 출처와 라이선스

이 자료에 들어 있는 논문 PDF와 논문 그림은 모두 오픈 액세스이며, 아래 라이선스에 따라 포함했다. 라이선스는 각 PDF 마지막 쪽의 Open Access 문구로 확인했다.

## backup_pdf/ — 논문 PDF 5편

| 파일 | 논문 | DOI | 라이선스 |
|---|---|---|---|
| `00_Park_2025.pdf` | Park et al., "Field-programmable robotic folding sheet", *Nature Communications* 16, 6937 (2025) | [10.1038/s41467-025-61838-3](https://doi.org/10.1038/s41467-025-61838-3) | [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) |
| `05_Yan_2023.pdf` | Yan et al., "Origami-based integration of robots that sense, decide, and respond", *Nature Communications* 14, 1553 (2023) | [10.1038/s41467-023-37158-9](https://doi.org/10.1038/s41467-023-37158-9) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| `08_Zhang_2023.pdf` | Zhang et al., "Plug & play origami modules with all-purpose deformation modes", *Nature Communications* 14, 4329 (2023) | [10.1038/s41467-023-39980-7](https://doi.org/10.1038/s41467-023-39980-7) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| `10_Johnson_2023.pdf` | Johnson et al., "A multifunctional soft robotic shape display with high-speed actuation, sensing, and control", *Nature Communications* 14, 4516 (2023) | [10.1038/s41467-023-39842-2](https://doi.org/10.1038/s41467-023-39842-2) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| `48_Ni_2022.pdf` | Ni et al., "Soft shape-programmable surfaces by fast electromagnetic actuation of liquid metal networks", *Nature Communications* 13, 5576 (2022) | [10.1038/s41467-022-31092-y](https://doi.org/10.1038/s41467-022-31092-y) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |

PDF는 출판사가 배포한 파일 그대로다. `seed_papers.csv`의 6번째 논문(Liu 2021, *Science Robotics*)은 오픈 액세스가 아니어서 포함하지 않았다.

## example_run/explainer/figures/ — 논문 그림 11장

| 파일 | 원 그림 | 사용 범위 | 라이선스 |
|---|---|---|---|
| `park2025_fig1.jpg` – `park2025_fig5.jpg` | Park 2025, Fig. 1–5 | 그림 전체, 변경 없음 | CC BY-NC-ND 4.0 |
| `zhang2023_fig2a.jpg` | Zhang 2023, Fig. 2a | 일부 발췌 (패널 a) | CC BY 4.0 |
| `ni2022_fig1a-f.jpg` | Ni 2022, Fig. 1a–f | 일부 발췌 (패널 a–f) | CC BY 4.0 |
| `ni2022_fig5.jpg` | Ni 2022, Fig. 5 | 그림 전체 | CC BY 4.0 |
| `johnson2023_fig1b-e.jpg` | Johnson 2023, Fig. 1b–e | 일부 발췌 (패널 b–e) | CC BY 4.0 |
| `johnson2023_fig4a-d.jpg` | Johnson 2023, Fig. 4a–d | 일부 발췌 (패널 a–d) | CC BY 4.0 |
| `yan2023_fig5a-i.jpg` | Yan 2023, Fig. 5a–i | 일부 발췌 (패널 a–i) | CC BY 4.0 |

- 그림은 출판사 PDF의 해당 영역을 이미지로 옮긴 것이다. 원문 캡션은 옮기지 않았다.
- CC BY-NC-ND 4.0인 Park 2025 그림은 자르거나 고치지 않았다. 이 라이선스는 비영리 목적의 원형 그대로의 재배포만 허용한다.
- CC BY 4.0 그림은 필요한 패널만 잘랐고, `park2025.html`에 "일부 발췌"와 출처를 표시했다.
- `guide_img/06e_figures.png`, `06f_claim1.png`, `06g_claim1_new.png`는 위 그림이 보이는 화면이다. 출처와 라이선스는 위 표와 같다.

## 이 표를 다시 만들 때

라이선스는 `reference/papers/collection_status.csv`의 `license` 열(OpenAlex 조회 결과)과 각 PDF 마지막 쪽의 Open Access 문구가 일치하는지 확인해 적는다.
