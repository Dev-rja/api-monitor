# API Reliability Monitor — SLA Report

> Last updated: **2026-05-04 22:36 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 59.03% | 4290.4 | 10206.7 | 1000ms | 261/637 |
| ❌ | `public_apis_list` | 0.0% | 99.69% | 122.3 | 4088.9 | 1500ms | 2/637 |
| ❌ | `nasa_apod` | 70.96% | 49.92% | 3514.7 | 10549.1 | 2000ms | 319/637 |
| ❌ | `ipapi_check` | 86.97% | 100.0% | 156.1 | 353.0 | 2500ms | 0/637 |
| ⚠️ | `rest_countries` | 98.59% | 98.27% | 341.2 | 10221.5 | 2500ms | 11/637 |
| ⚠️ | `open_meteo_weather` | 98.74% | 96.7% | 727.0 | 14877.1 | 2000ms | 21/637 |
| ⚠️ | `dog_ceo_random` | 99.53% | 93.41% | 704.9 | 10244.1 | 2500ms | 42/637 |
| ✅ | `catfact_random` | 99.53% | 99.37% | 255.3 | 10080.2 | 3000ms | 4/637 |
| ✅ | `coingecko_bitcoin` | 99.53% | 100.0% | 98.5 | 252.0 | 1500ms | 0/637 |
| ✅ | `useless_fact` | 99.69% | 99.37% | 590.7 | 10229.6 | 2500ms | 4/637 |
| ✅ | `agify_name` | 100.0% | 99.84% | 369.6 | 3237.1 | 2000ms | 1/637 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.69% | 237.4 | 3882.8 | 2000ms | 2/637 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 5605.3 | 54.55% |
| `numbers_trivia` | 03:00 | 5199.6 | 50.0% |
| `numbers_trivia` | 12:00 | 5183.8 | 50.0% |
| `numbers_trivia` | 01:00 | 5126.1 | 50.0% |
| `nasa_apod` | 03:00 | 5080.8 | 81.25% |
| `numbers_trivia` | 07:00 | 4955.2 | 47.62% |
| `nasa_apod` | 17:00 | 4828.5 | 59.46% |
| `numbers_trivia` | 10:00 | 4784.8 | 46.15% |
| `numbers_trivia` | 05:00 | 4708.1 | 45.0% |
| `numbers_trivia` | 18:00 | 4677.8 | 44.83% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
