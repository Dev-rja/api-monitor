# API Reliability Monitor — SLA Report

> Last updated: **2026-05-06 13:11 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 60.27% | 4166.6 | 10206.7 | 1000ms | 261/657 |
| ❌ | `public_apis_list` | 0.0% | 99.54% | 129.0 | 4595.4 | 1500ms | 3/657 |
| ❌ | `nasa_apod` | 71.84% | 51.45% | 3422.2 | 10549.1 | 2000ms | 319/657 |
| ❌ | `ipapi_check` | 86.91% | 100.0% | 156.5 | 363.0 | 2500ms | 0/657 |
| ⚠️ | `rest_countries` | 98.63% | 98.33% | 337.5 | 10221.5 | 2500ms | 11/657 |
| ⚠️ | `open_meteo_weather` | 98.78% | 96.8% | 721.5 | 14877.1 | 2000ms | 21/657 |
| ⚠️ | `dog_ceo_random` | 99.54% | 93.61% | 697.1 | 10244.1 | 2500ms | 42/657 |
| ✅ | `catfact_random` | 99.54% | 99.39% | 260.8 | 10080.2 | 3000ms | 4/657 |
| ✅ | `coingecko_bitcoin` | 99.54% | 100.0% | 98.4 | 252.0 | 1500ms | 0/657 |
| ✅ | `useless_fact` | 99.7% | 99.39% | 593.8 | 10229.6 | 2500ms | 4/657 |
| ✅ | `agify_name` | 100.0% | 99.85% | 369.1 | 3237.1 | 2000ms | 1/657 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.7% | 236.7 | 3882.8 | 2000ms | 2/657 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5199.6 | 50.0% |
| `numbers_trivia` | 12:00 | 5183.8 | 50.0% |
| `numbers_trivia` | 00:00 | 5152.0 | 50.0% |
| `nasa_apod` | 03:00 | 5080.8 | 81.25% |
| `numbers_trivia` | 07:00 | 4955.2 | 47.62% |
| `nasa_apod` | 17:00 | 4716.3 | 57.89% |
| `numbers_trivia` | 05:00 | 4708.1 | 45.0% |
| `numbers_trivia` | 01:00 | 4686.2 | 45.45% |
| `numbers_trivia` | 10:00 | 4616.5 | 44.44% |
| `numbers_trivia` | 18:00 | 4526.1 | 43.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
