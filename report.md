# API Reliability Monitor — SLA Report

> Last updated: **2026-05-01 05:11 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 54.37% | 4752.3 | 10206.7 | 1000ms | 261/572 |
| ❌ | `public_apis_list` | 0.0% | 99.65% | 123.1 | 4088.9 | 1500ms | 2/572 |
| ❌ | `nasa_apod` | 67.83% | 44.76% | 3839.8 | 10549.1 | 2000ms | 316/572 |
| ❌ | `ipapi_check` | 87.59% | 100.0% | 156.1 | 353.0 | 2500ms | 0/572 |
| ⚠️ | `rest_countries` | 98.43% | 98.25% | 349.3 | 10221.5 | 2500ms | 10/572 |
| ⚠️ | `open_meteo_weather` | 98.6% | 97.2% | 721.2 | 14877.1 | 2000ms | 16/572 |
| ⚠️ | `dog_ceo_random` | 99.48% | 92.66% | 742.8 | 10244.1 | 2500ms | 42/572 |
| ✅ | `catfact_random` | 99.48% | 99.48% | 251.3 | 10080.2 | 3000ms | 3/572 |
| ✅ | `useless_fact` | 99.65% | 99.3% | 584.6 | 10229.6 | 2500ms | 4/572 |
| ✅ | `coingecko_bitcoin` | 99.65% | 100.0% | 99.2 | 252.0 | 1500ms | 0/572 |
| ✅ | `agify_name` | 100.0% | 99.83% | 370.6 | 3237.1 | 2000ms | 1/572 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.65% | 238.8 | 3882.8 | 2000ms | 2/572 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6148.6 | 60.0% |
| `numbers_trivia` | 03:00 | 5523.2 | 53.33% |
| `numbers_trivia` | 07:00 | 5456.4 | 52.63% |
| `nasa_apod` | 03:00 | 5403.4 | 86.67% |
| `numbers_trivia` | 18:00 | 5398.4 | 52.0% |
| `numbers_trivia` | 10:00 | 5392.0 | 52.17% |
| `numbers_trivia` | 12:00 | 5382.0 | 52.0% |
| `nasa_apod` | 17:00 | 5367.0 | 66.67% |
| `numbers_trivia` | 01:00 | 5126.1 | 50.0% |
| `numbers_trivia` | 14:00 | 5027.1 | 48.39% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
