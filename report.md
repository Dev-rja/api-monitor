# API Reliability Monitor — SLA Report

> Last updated: **2026-04-30 23:35 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 54.21% | 4768.6 | 10206.7 | 1000ms | 261/570 |
| ❌ | `public_apis_list` | 0.0% | 99.65% | 123.3 | 4088.9 | 1500ms | 2/570 |
| ❌ | `nasa_apod` | 67.72% | 44.74% | 3846.5 | 10549.1 | 2000ms | 315/570 |
| ❌ | `ipapi_check` | 87.54% | 100.0% | 156.3 | 353.0 | 2500ms | 0/570 |
| ⚠️ | `rest_countries` | 98.42% | 98.25% | 349.7 | 10221.5 | 2500ms | 10/570 |
| ⚠️ | `open_meteo_weather` | 98.6% | 97.19% | 721.3 | 14877.1 | 2000ms | 16/570 |
| ⚠️ | `dog_ceo_random` | 99.47% | 92.63% | 743.7 | 10244.1 | 2500ms | 42/570 |
| ✅ | `catfact_random` | 99.47% | 99.47% | 251.6 | 10080.2 | 3000ms | 3/570 |
| ✅ | `useless_fact` | 99.65% | 99.3% | 583.8 | 10229.6 | 2500ms | 4/570 |
| ✅ | `coingecko_bitcoin` | 99.65% | 100.0% | 99.2 | 252.0 | 1500ms | 0/570 |
| ✅ | `agify_name` | 100.0% | 99.82% | 369.4 | 3237.1 | 2000ms | 1/570 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.65% | 238.9 | 3882.8 | 2000ms | 2/570 |

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
