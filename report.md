# API Reliability Monitor — SLA Report

> Last updated: **2026-04-24 20:26 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 58.64% | 4349.4 | 10206.7 | 1000ms | 194/469 |
| ❌ | `public_apis_list` | 0.0% | 99.57% | 128.3 | 4088.9 | 1500ms | 2/469 |
| ❌ | `nasa_apod` | 61.62% | 36.46% | 4434.1 | 10549.1 | 2000ms | 298/469 |
| ❌ | `ipapi_check` | 93.18% | 100.0% | 158.4 | 353.0 | 2500ms | 0/469 |
| ⚠️ | `open_meteo_weather` | 98.29% | 97.01% | 733.5 | 14877.1 | 2000ms | 14/469 |
| ⚠️ | `rest_countries` | 98.51% | 98.08% | 357.0 | 10221.5 | 2500ms | 9/469 |
| ⚠️ | `dog_ceo_random` | 99.36% | 91.04% | 822.0 | 10244.1 | 2500ms | 42/469 |
| ✅ | `catfact_random` | 99.36% | 99.36% | 265.9 | 10080.2 | 3000ms | 3/469 |
| ✅ | `useless_fact` | 99.57% | 99.15% | 584.2 | 10229.6 | 2500ms | 4/469 |
| ✅ | `agify_name` | 100.0% | 99.79% | 373.5 | 3237.1 | 2000ms | 1/469 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.79% | 235.8 | 2314.9 | 2000ms | 1/469 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.9 | 252.0 | 1500ms | 0/469 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `nasa_apod` | 17:00 | 5806.4 | 71.43% |
| `nasa_apod` | 18:00 | 5779.3 | 85.71% |
| `nasa_apod` | 03:00 | 5600.9 | 85.71% |
| `nasa_apod` | 11:00 | 5359.7 | 64.29% |
| `numbers_trivia` | 12:00 | 5201.9 | 50.0% |
| `numbers_trivia` | 03:00 | 5200.2 | 50.0% |
| `nasa_apod` | 00:00 | 5195.1 | 75.0% |
| `numbers_trivia` | 18:00 | 4987.3 | 47.62% |
| `nasa_apod` | 01:00 | 4971.7 | 60.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
