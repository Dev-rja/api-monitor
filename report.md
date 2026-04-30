# API Reliability Monitor — SLA Report

> Last updated: **2026-04-30 20:46 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 53.97% | 4793.4 | 10206.7 | 1000ms | 261/567 |
| ❌ | `public_apis_list` | 0.0% | 99.65% | 123.1 | 4088.9 | 1500ms | 2/567 |
| ❌ | `nasa_apod` | 67.55% | 44.44% | 3864.5 | 10549.1 | 2000ms | 315/567 |
| ❌ | `ipapi_check` | 87.48% | 100.0% | 156.3 | 353.0 | 2500ms | 0/567 |
| ⚠️ | `rest_countries` | 98.41% | 98.24% | 350.6 | 10221.5 | 2500ms | 10/567 |
| ⚠️ | `open_meteo_weather` | 98.59% | 97.18% | 722.5 | 14877.1 | 2000ms | 16/567 |
| ⚠️ | `dog_ceo_random` | 99.47% | 92.59% | 745.7 | 10244.1 | 2500ms | 42/567 |
| ✅ | `catfact_random` | 99.47% | 99.47% | 252.1 | 10080.2 | 3000ms | 3/567 |
| ✅ | `useless_fact` | 99.65% | 99.29% | 583.8 | 10229.6 | 2500ms | 4/567 |
| ✅ | `coingecko_bitcoin` | 99.65% | 100.0% | 99.4 | 252.0 | 1500ms | 0/567 |
| ✅ | `agify_name` | 100.0% | 99.82% | 369.3 | 3237.1 | 2000ms | 1/567 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.65% | 239.0 | 3882.8 | 2000ms | 2/567 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6148.6 | 60.0% |
| `numbers_trivia` | 01:00 | 5682.4 | 55.56% |
| `numbers_trivia` | 03:00 | 5523.2 | 53.33% |
| `numbers_trivia` | 07:00 | 5456.4 | 52.63% |
| `nasa_apod` | 03:00 | 5403.4 | 86.67% |
| `numbers_trivia` | 18:00 | 5398.4 | 52.0% |
| `numbers_trivia` | 10:00 | 5392.0 | 52.17% |
| `numbers_trivia` | 12:00 | 5382.0 | 52.0% |
| `nasa_apod` | 17:00 | 5367.0 | 66.67% |
| `numbers_trivia` | 05:00 | 5217.3 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
